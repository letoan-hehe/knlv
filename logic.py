import pandas as pd
import streamlit as st
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# --- CÁC HÀM XỬ LÝ DỮ LIỆU ---
def max_day(df, date_col):
    date_series = pd.to_datetime(df[date_col], errors='coerce')
    if date_series.empty:
        return dt.date.today()
    return date_series.max().date()

def min_day(df, date_col):
    date_series = pd.to_datetime(df[date_col], errors='coerce')
    if date_series.empty:
        return dt.date.today()
    return date_series.min().date()

def filter_data(df, date_col, start_date, end_date, state_col, selected_state, city_col, selected_city):
    df_filter = df.copy()
    if date_col in df_filter.columns:
        df_filter[date_col] = pd.to_datetime(df_filter[date_col], dayfirst=True, errors='coerce')
        mask = (df_filter[date_col].dt.date >= start_date) & (df_filter[date_col].dt.date <= end_date)
        df_filter = df_filter.loc[mask]
    
    if state_col in df_filter.columns and selected_state:
        df_filter = df_filter[df_filter[state_col].isin(selected_state)]
        
    if city_col in df_filter.columns and selected_city:
        df_filter = df_filter[df_filter[city_col].isin(selected_city)]
        
    return df_filter

def reset_day():
    if 'df_dulieu' in st.session_state and st.session_state['df_dulieu'] is not None:
        df = st.session_state['df_dulieu']
        if 'Ngày đặt hàng' in df.columns:
            default_start = min_day(df, 'Ngày đặt hàng')
            default_end   = max_day(df, 'Ngày đặt hàng')
            
            st.session_state['start_date'] = default_start
            st.session_state['end_date']   = default_end
            
            # Buộc widget cập nhật lại
            st.session_state['start_date_widget'] = default_start
            st.session_state['end_date_widget']   = default_end

def to_datetime(date_input):
    if isinstance(date_input, dt.date):
        return pd.to_datetime(date_input)
    return pd.to_datetime(date_input, errors='coerce')

def smart_format(value):
    try:
        val = float(value)
    except:
        return str(value)
    abs_val = abs(val)
    if abs_val >= 1_000_000_000:
        return f'{val / 1_000_000_000:,.2f}B'
    elif abs_val >= 1_000_000:
        return f'{val / 1_000_000:,.2f}M'
    elif abs_val >= 1_000:
        return f'{val / 1_000:,.1f}K'
    else:
        return f'{val:,.0f}' if val % 1 == 0 else f'{val:,.2f}'

# --- CÁC HÀM VẼ BIỂU ĐỒ ---

# 1. Hàm Aggregate Data (cho Trang 2)
def aggregate_data(df, x_col, y_col, agg_type):
    agg_map = {
        'Tổng (Sum)': 'sum', 'Trung bình (Mean)': 'mean',
        'Lớn nhất (Max)': 'max', 'Nhỏ nhất (Min)': 'min', 'Đếm số lượng (Count)': 'count'
    }
    method = agg_map.get(agg_type, 'sum')
    if method == 'count':
        df_res = df.groupby(x_col)[x_col].count().reset_index(name='Giá trị')
        fmt = '{:,.0f}'
    else:
        df_res = df.groupby(x_col)[y_col].agg(method).reset_index()
        df_res.rename(columns={y_col: 'Giá trị'}, inplace=True)
        fmt = '{:,.2f}'
    return df_res.sort_values(by='Giá trị', ascending=False), fmt

# 2. Biểu đồ Cột đứng (Cập nhật: Thêm tham số color)
def bar_chart(x_col, y_col, title='Bar chart', xlabel='Danh mục', ylabel='Giá trị', show_value=True, fmt=None, color='#1f77b4'):
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    # Sử dụng tham số color được truyền vào
    bars = ax.bar(x_col, y_col, width=0.5, alpha=0.8, color=color)
    
    if not y_col.empty:
        ax.set_ylim(0, y_col.max() * 1.15)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.tick_params(axis='x', rotation=45)
    
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, pos: smart_format(x)))

    if show_value:
        for bar in bars:
            height = bar.get_height()
            label = smart_format(height)
            xy_pos = (bar.get_x() + bar.get_width() / 2, height)
            text_pos = (0, 5) if height >= 0 else (0, -15)
            va_align = 'bottom' if height >= 0 else 'top'
            
            ax.annotate(label, xy=xy_pos, xytext=text_pos, textcoords="offset points",
                        ha='center', va=va_align, fontsize=9)
    plt.tight_layout()
    return fig

# 3. Biểu đồ Đường
def line_chart(x_col, y_col, title='Line chart', xlabel='Thời gian', ylabel='Giá trị', show_value=True, fmt=None):
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    ax.plot(x_col, y_col, marker='o', linestyle='-', color='#ff7f0e', linewidth=2)
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(axis='y', linestyle='--', alpha=0.8)
    ax.tick_params(axis='x', rotation=45)
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, pos: smart_format(x)))
    
    if show_value:
        step = 1 if len(y_col) < 15 else len(y_col) // 10
        for i in range(0, len(y_col), step):
            val = y_col.iloc[i]
            ax.annotate(smart_format(val), (x_col.iloc[i], val), 
                        textcoords="offset points", xytext=(0, 8), ha='center', fontsize=8,
                        bbox=dict(boxstyle="round,pad=0.2", fc="white", alpha=0.7, ec="none"))
    plt.tight_layout()
    return fig

# 4. Biểu đồ Cột Ngang
def bar_chart_2(x_col, y_col, title=None, xlabel='Giá trị', ylabel='Danh mục', show_value=True, color=None, fmt=None):
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    bars = ax.barh(x_col, y_col, height=0.5, alpha=0.8, color=color)
    
    if not y_col.empty:
        max_val = y_col.max()
        ax.set_xlim(0, max_val * 1.15) 
        
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.tick_params(axis='x', rotation=0)
    ax.xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, pos: smart_format(x)))
    ax.invert_yaxis()
    
    if show_value:
        for bar in bars:
            width = bar.get_width()
            ax.text(width, bar.get_y() + bar.get_height()/2, f' {smart_format(width)}', va='center', fontsize=9)
    plt.tight_layout()
    return fig

# 5. Biểu đồ Tròn
def pie_chart(x_col, y_col, title='Pie chart'):
    if len(y_col) > 10:
        df_temp = pd.DataFrame({'label': x_col, 'value': y_col})
        df_head = df_temp.head(5)
        other_val = df_temp['value'][5:].sum()
        new_row = pd.DataFrame([{'label': 'Khác', 'value': other_val}])
        df_plot = pd.concat([df_head, new_row], ignore_index=True)
        labels = df_plot['label']
        values = df_plot['value']
    else:
        labels = x_col
        values = y_col

    fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
    wedges, texts, autotexts = ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    ax.axis('equal')
    ax.set_title(title)
    plt.tight_layout()
    return fig