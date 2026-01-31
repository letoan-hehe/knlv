import streamlit as st
import pandas as pd
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import time
import logic
from datetime import datetime, date

#Hiển thị trang bìa
REQUIRED_COLUMNS = [
    "Ngày đặt hàng",
    "Sản phẩm",
    "Số lượng bán",
    "Danh mục",
    "Khu vực",
    "Tỉnh",
    "Doanh thu",
    "Giá vốn",
    "Lợi nhuận",
    "Đánh giá"
]

data_mau = {
                    "ID": range(1, 16),
                    "Ngày đặt hàng": [
                        "01/01/2024", "02/01/2024", "05/01/2024", "08/01/2024", "12/01/2024",
                        "01/02/2024", "14/02/2024", "20/02/2024", "25/02/2024", "05/03/2024",
                        "10/03/2024", "15/03/2024", "20/03/2024", "01/04/2024", "10/04/2024"
                    ],
                    "Sản phẩm": [
                        "Laptop Dell", "Chuột Logitech", "Tai nghe Sony", "Màn hình LG", "Laptop Asus",
                        "Iphone 15", "Samsung S24", "Loa JBL", "Bàn phím cơ", "Macbook Air",
                        "Chuột Gaming", "Ghế Công thái học", "Webcam 4K", "Microphone", "Pad chuột"
                    ],
                    "Số lượng bán": [5, 50, 20, 10, 8, 15, 12, 25, 30, 6, 40, 5, 10, 15, 60],
                    "Danh mục": [
                        "Máy tính", "Phụ kiện", "Âm thanh", "Màn hình", "Máy tính",
                        "Điện thoại", "Điện thoại", "Âm thanh", "Phụ kiện", "Máy tính",
                        "Phụ kiện", "Nội thất", "Phụ kiện", "Âm thanh", "Phụ kiện"
                    ],
                    "Khu vực": [
                        "Miền Bắc", "Miền Nam", "Miền Trung", "Miền Bắc", "Miền Nam",
                        "Miền Nam", "Miền Bắc", "Miền Trung", "Miền Bắc", "Miền Nam",
                        "Miền Trung", "Miền Bắc", "Miền Nam", "Miền Bắc", "Miền Trung"
                    ],
                    "Tỉnh": [
                        "Hà Nội", "TP.HCM", "Đà Nẵng", "Hải Phòng", "Bình Dương",
                        "Cần Thơ", "Hà Nội", "Nghệ An", "Quảng Ninh", "TP.HCM",
                        "Huế", "Hà Nội", "Đồng Nai", "Bắc Ninh", "Thanh Hóa"
                    ],
                    "Doanh thu": [
                        100000000, 25000000, 40000000, 50000000, 120000000,
                        450000000, 360000000, 50000000, 30000000, 150000000,
                        20000000, 25000000, 15000000, 30000000, 6000000
                    ],
                    "Giá vốn": [
                        80000000, 15000000, 25000000, 35000000, 100000000,
                        380000000, 300000000, 35000000, 20000000, 120000000,
                        12000000, 15000000, 10000000, 20000000, 3000000
                    ],
                    "Lợi nhuận": [
                        20000000, 10000000, 15000000, 15000000, 20000000,
                        70000000, 60000000, 15000000, 10000000, 30000000,
                        8000000, 10000000, 5000000, 10000000, 3000000
                    ],
                    "Đánh giá": [5, 4, 4.5, 5, 4, 5, 4.5, 4, 5, 5, 3.5, 4, 4.5, 4, 5]
                }


def kiem_tra_cot_bat_buoc(df):
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    return missing_cols

def hien_thi_man_hinh_cho():
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.write('<br><br>', unsafe_allow_html=True)
        st.title('📊 Nhập dữ liệu kinh doanh')
        st.write('Kéo thả file CSV của bạn vào dưới hoặc chọn **Dữ liệu mẫu** để xem thử dashboard.')

        st.divider()

        # Hàm xóa bộ lọc (Force Reset)
        def clear_filters():
            keys_to_clear = ['start_date', 'end_date', 'chon_khu_vuc', 'chon_tinh']
            for key in keys_to_clear:
                if key in st.session_state:
                    del st.session_state[key]

        col_mau_1, col_mau_2 = st.columns(2)
        
        with col_mau_1:
            df_template = pd.DataFrame(columns=REQUIRED_COLUMNS)
            csv_template = df_template.to_csv(index=False, encoding="utf-8-sig")
            st.download_button(
                label="⬇ Tải file mẫu trắng (CSV)",
                data=csv_template,
                file_name="template_data.csv",
                mime="text/csv",
                use_container_width=True
            )

        with col_mau_2:
            if st.button("🚀 Dùng Dữ liệu Mẫu (Test ngay)", type="primary", use_container_width=True):
                
                df_mau = pd.DataFrame(data_mau)
                st.session_state['df_dulieu'] = df_mau
                st.session_state['is_standard_file'] = True
                
                # --- QUAN TRỌNG: RESET BỘ LỌC ---
                clear_filters()
                
                st.success("✅ Đã nạp 15 dòng dữ liệu mẫu!")
                time.sleep(0.5)
                st.rerun()

        st.write("---") 

        # ================= UPLOAD FILE THẬT =================
        uploaded_file = st.file_uploader("Hoặc tải file CSV dữ liệu của bạn", type=['csv'])

        if uploaded_file is not None:
            with st.spinner('Đang xử lý...'):
                try:
                    # 1. Đọc dữ liệu tạm thời
                    df_temp = pd.read_csv(uploaded_file, sep=None, engine="python", encoding="utf-8-sig")
                    df_temp.columns = df_temp.columns.str.strip()
                    
                    # 2. Xử lý ngày tháng
                    if 'Ngày đặt hàng' in df_temp.columns:
                        df_temp['Ngày đặt hàng'] = pd.to_datetime(df_temp['Ngày đặt hàng'], dayfirst=True, errors='coerce')
                        df_temp = df_temp.dropna(subset=['Ngày đặt hàng'])
                    
                    # 3. Kiểm tra cột
                    missing_cols = kiem_tra_cot_bat_buoc(df_temp)
                    
                    if missing_cols:
                        # Hiển thị lỗi rõ ràng và KHÔNG lưu vào session_state
                        st.error(f"❌ File không hợp lệ! Thiếu các cột: {', '.join(missing_cols)}")
                        st.info("Vui lòng kiểm tra lại file CSV hoặc tải file mẫu bên trên.")
                    else:
                        # 4. Nếu mọi thứ OK mới lưu vào session_state và chuyển trang
                        st.session_state['df_dulieu'] = df_temp
                        st.session_state['is_standard_file'] = True
                        clear_filters()
                        
                        st.success('✅ File hợp lệ! Đang chuyển hướng...')
                        time.sleep(1)
                        st.rerun()

                except Exception as e:
                    st.error(f'Lỗi định dạng file: {e}')

# Hiển thị das
def hien_thi_dashboard():
    df = st.session_state['df_dulieu']
    df = st.session_state['df_dulieu']
    
    # --- BƯỚC CHUẨN BỊ (PHẢI CÓ CÁI NÀY THÌ MỚI HẾT LỖI) ---
    df_cal = df.copy()
    # Ép kiểu ngày tháng để tính toán danh sách tháng
    df_cal['Ngày đặt hàng'] = pd.to_datetime(df_cal['Ngày đặt hàng'], dayfirst=True, errors='coerce')
    df_cal = df_cal.dropna(subset=['Ngày đặt hàng'])
    
    # Tạo cột phụ để dễ so sánh
    df_cal['Thang_Int'] = df_cal['Ngày đặt hàng'].dt.month.astype(int)
    df_cal['Nam_Int'] = df_cal['Ngày đặt hàng'].dt.year.astype(int)
    
    # Đây chính là "danh_sach_thang" fen đang tìm:
    # Lấy các cặp Năm-Tháng duy nhất và sắp xếp từ cũ đến mới
    danh_sach_thang = df_cal[['Nam_Int', 'Thang_Int']].drop_duplicates().sort_values(['Nam_Int', 'Thang_Int']).values.tolist()
    with st.sidebar:
        st.title('🏠 Menu Hệ thống')
        trang = st.radio('Chon trang',options=['Trang 1','Trang 2'], index= 0,key="navigation_radio")
        if st.button('Tải file khác'):
            st.session_state['df_dulieu'] = None
            st.rerun()
        
        if 'start_date' not in st.session_state:
            st.session_state['start_date'] = logic.min_day(df, 'Ngày đặt hàng')
        if 'end_date' not in st.session_state:
            st.session_state['end_date'] = logic.max_day(df, 'Ngày đặt hàng')
        if 'start_date_widget' not in st.session_state:
            st.session_state['start_date_widget'] = st.session_state['start_date']

        if 'end_date_widget' not in st.session_state:
            st.session_state['end_date_widget'] = st.session_state['end_date']
                
    with st.sidebar:
            st.header('Công cụ phân tích')
            st.button('Đặt lại ngày', on_click= logic.reset_day)
            d_min = logic.min_day(df, 'Ngày đặt hàng')
            d_max = logic.max_day(df, 'Ngày đặt hàng')

            # Đảm bảo session_state cũng lưu trữ đúng kiểu date, không lưu NaT
            if 'start_date' not in st.session_state or pd.isna(st.session_state['start_date']):
                st.session_state['start_date'] = d_min
            if 'end_date' not in st.session_state or pd.isna(st.session_state['end_date']):
                st.session_state['end_date'] = d_max
            with st.expander(" Bộ lọc Thời gian", expanded=True):
                col1, col2 = st.columns(2)
                with col1:
                    start_str = st.date_input("Từ ngày",
                        # value=d_min,
                        min_value=d_min,
                        max_value=d_max,
                        format="DD/MM/YYYY", key='start_date_widget')
                with col2:
                    end_str = st.date_input("Đến ngày",
                        # value=d_min,
                        min_value=d_min,
                        max_value=d_max,
                        format="DD/MM/YYYY", key='end_date_widget') 
            
            with st.expander(" Bộ lọc Khu vực", expanded=False):
                col3, col4 = st.columns([1,1])
                with col3:
                    khu_vuc_list = df['Khu vực'].dropna().unique()
                    selected_khu_vuc = st.multiselect('Chọn khu vực', khu_vuc_list,key='chon_khu_vuc')

                with col4:
                    if selected_khu_vuc:
                        tinh_list = df[df['Khu vực'].isin(selected_khu_vuc)]['Tỉnh'].dropna().unique()
                    else:
                        tinh_list = df['Tỉnh'].dropna().unique()
                    selected_tinh = st.multiselect('Chọn tỉnh', tinh_list,key='chon_tinh')
            st.markdown('---')

    if trang == 'Trang 1':
        st.title('📊 Dashboard Tổng quan kinh doanh')
        
        # --- LỌC DỮ LIỆU HIỂN THỊ (THEO BỘ LỌC) ---
        df_da_loc = logic.filter_data(df, 'Ngày đặt hàng', start_str, end_str,
                                      'Khu vực', selected_khu_vuc, 'Tỉnh', selected_tinh)
        
        if df_da_loc.empty:
            st.warning("Không có dữ liệu phù hợp với bộ lọc hiện tại. Vui lòng chọn lại!")
            return

        # ================= TÍNH TOÁN METRIC (FIX LỖI TĂNG TRƯỞNG 4000%) =================
        try:
            # A. Con số chính: Tổng của toàn bộ vùng thời gian đang lọc (Ví dụ: Cả năm 2025)
            tong_dt = df_da_loc['Doanh thu'].sum()
            tong_ln = df_da_loc['Lợi nhuận'].sum()
            tong_sd = len(df_da_loc)

            # B. Tính Delta: Chỉ so sánh Tháng cuối cùng trong vùng lọc với Tháng ngay trước đó
            # Bước 1: Xác định tháng/năm mới nhất trong tập dữ liệu đã lọc
            thang_cuoi = pd.to_datetime(df_da_loc['Ngày đặt hàng']).max()
            curr_m, curr_y = thang_cuoi.month, thang_cuoi.year

            # Bước 2: Lấy giá trị của riêng tháng cuối đó để làm mốc "Hiện tại"
            mask_curr = (df_da_loc['Ngày đặt hàng'].dt.month == curr_m) & (df_da_loc['Ngày đặt hàng'].dt.year == curr_y)
            val_curr_dt = df_da_loc[mask_curr]['Doanh thu'].sum()
            val_curr_ln = df_da_loc[mask_curr]['Lợi nhuận'].sum()
            val_curr_sd = len(df_da_loc[mask_curr])

            # Bước 3: Tìm tháng có dữ liệu ngay trước đó trong file gốc (df_cal)
            # Chúng ta dùng df_cal đã chuẩn bị sẵn (đã ép kiểu datetime và lọc khu vực/tỉnh)
            dt_p = ln_p = sd_p = 0
            target = [curr_y, curr_m]
            
            if target in danh_sach_thang:
                idx = danh_sach_thang.index(target)
                if idx > 0:
                    y_p, m_p = danh_sach_thang[idx-1]
                    df_p = df_cal[(df_cal['Nam_Int'] == y_p) & (df_cal['Thang_Int'] == m_p)]
                    
                    # Tính toán mốc "Kỳ trước"
                    dt_p = df_p['Doanh thu'].sum()
                    ln_p = df_p['Lợi nhuận'].sum()
                    sd_p = len(df_p)
                    help_text = f"So sánh Tháng {curr_m}/{curr_y} vs Tháng {m_p}/{y_p}"
                else:
                    help_text = "Tháng đầu tiên của dữ liệu, không có kỳ trước để so sánh"
            
            # Hàm tính Delta an toàn
            def cal_delta(c, p):
                if p == 0: return "n/a"
                return f"{((c - p) / p) * 100:+.1f}%"

        except Exception as e:
            st.error(f"Lỗi tính toán: {e}")
            dt_p = ln_p = sd_p = 0
            help_text = "Lỗi định dạng dữ liệu"
    # --- HIỂN THỊ KPI ---
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("💰 Tổng Doanh Thu", f"{logic.smart_format(tong_dt)} VND", cal_delta(val_curr_dt, dt_p),help= help_text)
        with c2:
            st.metric("💹 Tổng Lợi Nhuận", f"{logic.smart_format(tong_ln)} VND", cal_delta(val_curr_ln, ln_p),help= help_text)
        with c3:
            st.metric("🧾 Tổng Đơn Hàng", f"{tong_sd:,} Đơn", cal_delta(val_curr_sd, sd_p),help= help_text)
            
        st.write('---')
        st.subheader('📊Biểu đồ phân tích📊')
        col_char1, col_chart2 = st.columns(2)

        # BIỂU ĐỒ 1: MÀU XANH LÁ
        data_chart = df_da_loc.groupby('Danh mục')['Doanh thu'].sum().reset_index()
        data_chart = data_chart.sort_values(by='Doanh thu', ascending=False)
        
        norm = mcolors.Normalize(vmin=data_chart['Doanh thu'].min(), vmax=data_chart['Doanh thu'].max())
        colors_green = cm.Greens(0.4 + 0.6 * norm(data_chart['Doanh thu'].values))

        with col_char1:
            fig = logic.bar_chart(
                data_chart['Danh mục'], 
                data_chart['Doanh thu'], 
                color=colors_green
            )
            st.pyplot(fig, use_container_width=True) # use_container_width để tự giãn

        # BIỂU ĐỒ 2: LINE CHART
        df_da_loc['Ngày đặt hàng'] = logic.to_datetime(df_da_loc['Ngày đặt hàng'])
        data_line = df_da_loc.set_index('Ngày đặt hàng').resample('M')['Doanh thu'].sum().reset_index()

        with col_chart2:
            fig2 = logic.line_chart(data_line['Ngày đặt hàng'], data_line['Doanh thu'])
            st.pyplot(fig2, use_container_width=True)

        # BIỂU ĐỒ 3 & 4
        col_chart3, col_chart4 = st.columns(2)
        data_chart1 = df_da_loc.groupby('Sản phẩm')['Doanh thu'].sum().reset_index()
        n_categories = data_chart1['Sản phẩm'].nunique()

        if n_categories <= 10:
            sorted_data_all = data_chart1.sort_values(by='Doanh thu', ascending=False)
            st.write(f"Chỉ có {n_categories} sản phẩm trong khu vực/thời gian này")
            fig = logic.bar_chart_2(
                sorted_data_all['Sản phẩm'],
                sorted_data_all['Doanh thu'],
                title='Doanh thu theo sản phẩm'
            )
            st.pyplot(fig, use_container_width=True)
        else:
            sorted_data_top = data_chart1.sort_values(by='Doanh thu', ascending=False).head(5)
            sorted_data_bot = data_chart1.sort_values(by='Doanh thu', ascending=True).head(5)[::-1]
            
            norm_top = mcolors.Normalize(vmin=sorted_data_top['Doanh thu'].min(), vmax=sorted_data_top['Doanh thu'].max())
            colors_top = cm.Greens(0.4 + 0.6 * norm_top(sorted_data_top['Doanh thu'].values))
            
            norm_bot = mcolors.Normalize(vmin=sorted_data_bot['Doanh thu'].min(), vmax=sorted_data_bot['Doanh thu'].max())
            colors_bot = cm.Reds_r(0.1 + 0.5 * norm_bot(sorted_data_bot['Doanh thu'].values))

            with col_chart3:
                fig3 = logic.bar_chart_2(
                    sorted_data_top['Sản phẩm'],
                    sorted_data_top['Doanh thu'],
                    title='Top 5 sản phẩm bán chạy',
                    color=colors_top
                )
                st.pyplot(fig3, use_container_width=True)

            with col_chart4:
                fig4 = logic.bar_chart_2(
                    sorted_data_bot['Sản phẩm'],
                    sorted_data_bot['Doanh thu'],
                    title='Top 5 sản phẩm bán kém',
                    color=colors_bot
                )
                st.pyplot(fig4, use_container_width=True)
    else:
        trang_2()

def trang_2():
    # Lấy dữ liệu từ session
    df = st.session_state.get('df_dulieu')
    
    if df is None:
        st.warning("⚠ Chưa có dữ liệu. Vui lòng quay lại Trang 1 để tải file lên.")
        return

    # ================= ÁP DỤNG BỘ LỌC =================
    start_date = st.session_state.get('start_date_widget')
    end_date = st.session_state.get('end_date_widget')
    khu_vuc = st.session_state.get('chon_khu_vuc', []) 
    tinh = st.session_state.get('chon_tinh', [])      

    df = logic.filter_data(
        df, 
        'Ngày đặt hàng', start_date, end_date,
        'Khu vực', khu_vuc,
        'Tỉnh', tinh
    )

    if df.empty:
        st.warning("Không có dữ liệu phù hợp với bộ lọc hiện tại!")
        return

    st.title("📊 Phân tích chi tiết tùy chỉnh")

    # ================= SIDEBAR: CẤU HÌNH =================
    with st.sidebar:
        st.header("🛠 Cấu hình biểu đồ")
        st.divider()
        
        # Phân loại cột
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        category_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

        if not numeric_cols or not category_cols:
            st.error("Dữ liệu cần có ít nhất 1 cột số và 1 cột phân loại!")
            return

        col_phan_loai = st.selectbox(
            "1️⃣ Chọn cột phân loại (Trục X):", 
            category_cols, 
            index=None, 
            placeholder="Vui lòng chọn cột..."
        )
        
        col_gia_tri = st.selectbox(
            "2️⃣ Chọn cột giá trị (Trục Y):", 
            numeric_cols, 
            index=None, 
            placeholder="Vui lòng chọn cột..."
        )

        st.write("3️⃣ Phương thức thống kê:")
        agg_option = st.selectbox(
            "Chọn phương thức:",
            ['Tổng (Sum)', 'Trung bình (Mean)', 'Lớn nhất (Max)', 'Nhỏ nhất (Min)', 'Đếm số lượng (Count)'],
            label_visibility="collapsed"
        )
        
        agg_func_map = {
            'Tổng (Sum)': 'sum',
            'Trung bình (Mean)': 'mean',
            'Lớn nhất (Max)': 'max',
            'Nhỏ nhất (Min)': 'min',
            'Đếm số lượng (Count)': 'count'
        }
        selected_agg = agg_func_map[agg_option]

        st.divider()
        chart_type = st.radio(
            "4️⃣ Chọn loại biểu đồ:", 
            ["Column (Cột)", "Line (Đường)", "Pie (Tròn)"]
        )

    # ================= HIỂN THỊ =================
    
    # ================= HIỂN THỊ =================
    if col_phan_loai and col_gia_tri:
        try:
            # 1. Xử lý dữ liệu
            if selected_agg == 'count':
                df_grouped = df.groupby(col_phan_loai)[col_phan_loai].count().reset_index(name='Giá trị')
                fmt = '{:,.0f}' # Số nguyên
            else:
                df_grouped = df.groupby(col_phan_loai)[col_gia_tri].agg(selected_agg).reset_index()
                df_grouped.rename(columns={col_gia_tri: 'Giá trị'}, inplace=True)
                fmt = '{:,.2f}' # Số thập phân

            df_grouped = df_grouped.sort_values(by='Giá trị', ascending=False)
            
            # Cắt giảm dữ liệu vẽ biểu đồ nếu quá nhiều (chỉ cho Bar/Line)
            df_plot = df_grouped.copy()
            if chart_type in ["Column (Cột)", "Line (Đường)"] and len(df_plot) > 30:
                st.caption(f"ℹ Hiển thị Top 15/{len(df_plot)} nhóm lớn nhất.")
                df_plot = df_plot.head(15)

        except Exception as e:
            st.error(f"Lỗi xử lý dữ liệu: {e}")
            return

        # 2. Vẽ Biểu đồ (GỌI HÀM TỪ LOGIC - Rất ngắn gọn)
        st.subheader(f"📊 Biểu đồ {chart_type}")
        
        if "Column" in chart_type:
            fig = logic.bar_chart(
                x_col=df_plot[col_phan_loai], 
                y_col=df_plot['Giá trị'],
                title=f"{agg_option} {col_gia_tri} theo {col_phan_loai}",
                xlabel=col_phan_loai,
                ylabel=agg_option,
                fmt=fmt # Truyền định dạng số vào
            )
            st.pyplot(fig)

        elif "Line" in chart_type:
            fig = logic.line_chart(
                x_col=df_plot[col_phan_loai], 
                y_col=df_plot['Giá trị'],
                title=f"{agg_option} {col_gia_tri} theo {col_phan_loai}",
                xlabel=col_phan_loai,
                ylabel=agg_option,
                fmt=fmt
            )
            st.pyplot(fig)

        elif "Pie" in chart_type:
            fig = logic.pie_chart(
                x_col=df_grouped[col_phan_loai],
                y_col=df_grouped['Giá trị'],
                title=f"Tỷ trọng {col_gia_tri} theo {col_phan_loai}"
            )
            st.pyplot(fig)

        st.divider()

        # 3. Bảng dữ liệu (Giữ nguyên)
        st.subheader("📋 Số liệu chi tiết")
        st.dataframe(
            df_grouped.style.format({'Giá trị': fmt}), 
            use_container_width=True,
            height=300
        )
        
        csv_data = df_grouped.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Tải kết quả (CSV)", csv_data, "ket_qua.csv", "text/csv")

    else:
        st.info("👈 Vui lòng chọn Trục X và Trục Y.")
        with st.expander("Xem trước dữ liệu thô"):
            st.dataframe(df, use_container_width=True, hide_index=True)