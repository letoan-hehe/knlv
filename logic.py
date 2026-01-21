import pandas as pd 
import streamlit as st
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
def max_day (df, date_col):
    date_series = pd.to_datetime (df[date_col], errors = 'coerce')
    return date_series.max().date()

def min_day (df, date_col):
    date_series = pd.to_datetime (df[date_col], errors = 'coerce')
    return date_series.min().date()

def pick_city (df, city_col, state_col, selected_state):
    if selected_state:
        filter_df= df[df[state_col].isin(selected_state)]
        return sorted(filter_df[city_col].unique().tolist())
    return sorted(df[city_col].unique().tolist())

def pick_state (df, state_col):
    return df[state_col].unique().tolist()

def filter_data (df, date_col, start_date, end_date, state_col, selected_state, city_col, selected_city):
    df[date_col] = pd.to_datetime(df[date_col], errors= 'coerce')
    mask = (df[date_col].dt.date >= start_date) & (df[date_col].dt.date <= end_date)
    df_filter = df.loc[mask]
    if selected_state:
        df_filter = df_filter[df_filter[state_col].isin(selected_state)]
    if selected_city:
        df_filter = df_filter[df_filter[city_col].isin(selected_city)]
    return df_filter

def reset_day():
    if 'df_dulieu' in st.session_state and st.session_state['df_dulieu'] is not None:
        df = st.session_state['df_dulieu']
        st.session_state['start_date'] = min_day(df,'Order Date')
        st.session_state['end_date'] = max_day(df,'Order Date')

def bar_chart ( x_col, y_col, title ='Bar chart', xlabel ='Category', ylabel = 'Value', show_value = True):
    fig, ax = plt.subplots(figsize = (10,6))
    bars = ax.bar(
    x_col, y_col,
    width = 0.4,
    alpha = 0.6,
)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(axis = 'y', linestyle ='--', alpha =0.5)
    ax.tick_params(axis = 'x', rotation = 45)
    ax.ticklabel_format(style ='plain', axis = 'y')
    ax.legend(bars, x_col)
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))
    if show_value:
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                f'{height:,.0f}',
                ha = 'center',
                va ='bottom',
                fontsize = 9
            )
    plt.tight_layout()
    return fig

def line_chart( x_col, y_col, title ='Line chart', xlabel ='Time', ylabel = 'Value', show_value = True):
    fig, ax = plt.subplots(figsize = (10,6))
    lines = ax.plot(
        x_col , y_col,
        marker ='o',
        linestyle = '-', 
    )
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(axis = 'y', linestyle ='--', alpha =0.5)
    ax.tick_params(axis = 'x', rotation = 45)
    ax.ticklabel_format(style ='plain', axis = 'y')
    
    plt.tight_layout()
    return fig

def to_datetime(date_input):
    if isinstance(date_input, dt.date):
        return pd.to_datetime(date_input)
    return pd.to_datetime(date_input, errors='coerce')