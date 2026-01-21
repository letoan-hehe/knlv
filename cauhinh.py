import streamlit as st
import pandas as pd
import time
import logic
from datetime import datetime, date

#Hiển thị trang bìa
def hien_thi_man_hinh_cho():
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.write('<br><br>', unsafe_allow_html = True)
        st.title ('Nhập dữ liệu kinh doanh')
        st.write ('Kéo thả file CSV vào bên dưới để hệ thống phân tích')

        #widget upload
        uploaded_file = st.file_uploader('',type=['csv'])

        #logic chuyển trang
        if uploaded_file is not None:
            with st.spinner('Đang tải dữ liệu...'):
                try:
                    if uploaded_file.name.endswith('.csv'):
                        df = pd.read_csv(uploaded_file, sep=';')
                    else:
                        st.error('Vui lòng chọn đúng file có định dạng csv')
                        st.stop()
                    st.session_state['df_dulieu'] = df
                    st.success ('Tải dữ liệu thành công!')
                    time.sleep(5)
                    st.rerun()
                except Exception as e:
                    st.error(f'File lỗi không đọc được: {e}')
# Hiển thị das
def hien_thi_dashboard():
    df = st.session_state['df_dulieu']
    with st.sidebar:
        st.header("Menu Hệ thống")
        trang = st.radio('Chon trang',options=['Trang 1','Trang 2'], index= 0,key="navigation_radio")
        st.divider()
    if trang =='Trang 1':
        hien_thi_trang1()
    else:
        trang_2()
def hien_thi_trang1():
    df = st.session_state['df_dulieu']
    if 'start_date' not in st.session_state:
        st.session_state['start_date'] = logic.min_day(df, 'Order Date')
    if 'end_date' not in st.session_state:
        st.session_state['end_date'] = logic.max_day(df, 'Order Date')
    with st.sidebar:
        st.header('Công cụ phân tích')
        st.success(f'File hợp lệ')
        st.button('Đặt lại ngày', on_click= logic.reset_day)
        
        # Slider chọn ngày
        col1, col2 = st.columns(2)
        with col1:
            start_str = st.date_input(
                "Từ ngày"
                ,min_value=logic.min_day(df,'Order Date')
                ,max_value = logic.max_day(df,'Order Date')
                ,format="DD/MM/YYYY"
                ,key='start_date' ) # Format hiển thị
        with col2:
            end_str = st.date_input(
                "Đến ngày"
                ,min_value=logic.min_day(df,'Order Date')
                ,max_value = logic.max_day(df,'Order Date')
                ,format="DD/MM/YYYY"
                ,key='end_date') 
        # Chọn bang và thành phố
        col3, col4 = st.columns([1,1])
        with col3:
            state = logic.pick_state(df,'State')
            selected_state = st.multiselect('Chọn bang', state, default = None)
        with col4:
            city = logic.pick_city(df,'City','State',selected_state)
            selected_city = st.multiselect('Chọn thành phố', city, default = None)
            
        st.markdown('---')
        # chọn file khác
        if st.button('Tải file khác'):
            st.session_state['df_dulieu'] = None
            st.rerun()
    # Tiêu đề
    st.title('Dashboard Tổng quan kinh doanh')
    df_da_loc = logic.filter_data(df,
                                  'Order Date',start_str,end_str,
                                  'State',selected_state,
                                  'City',selected_city)
    try:
        tong_doanh_thu = df_da_loc['Sales'].sum()
        tong_loi_nhuan = df_da_loc['Profit'].sum()
        so_don_hang = df_da_loc['Order ID'].count() 
    except KeyError as e:
        st.error(f"File CSV thiếu cột dữ liệu cần thiết: {e}")
        return

    # 3. Hiển thị KPI Cards
    col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
    with col_kpi1:
        st.metric(
            label="Tổng Doanh Thu", 
            value=f"{tong_doanh_thu:,.2f} $",
            
        )
    with col_kpi2:
        st.metric(
            label="Tổng Lợi Nhuận", 
            value=f"{tong_loi_nhuan:,.2f} $",
            delta=f"{tong_loi_nhuan/tong_doanh_thu*100:.1f}% " # Ví dụ thêm % biên lợi nhuận
        )
    with col_kpi3:
        st.metric(
            label="Số đơn hàng",
            value=f"{so_don_hang:,}"
        )
    # Hiển thị bảng dữ liệu chi tiết ở dưới 
    with st.expander("Xem chi tiết dữ liệu"):
        tong_sales = df_da_loc.groupby('Sub-Category')['Sales'].sum().reset_index()
        st.dataframe(tong_sales.style.format({'Sales' : '{:,.2f}'}), use_container_width=True)
    st.markdown('---')
    st.write('Bieu do phan tich')
    data_chart = df_da_loc.groupby('Category')['Sales'].sum().reset_index()
    fig = logic.bar_chart(data_chart['Category'], data_chart['Sales'])
    st.pyplot(fig)
def trang_2():
    df = st.session_state['df_dulieu']
    with st.sidebar:
        st.header("Menu Chi Tiết")
        st.warning("Đây là Sidebar của Trang 2 ")
        st.radio("Chọn loại biểu đồ:", ["Line", "Area"])




