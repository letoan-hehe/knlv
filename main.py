import streamlit as st
import pandas as pd

import cauhinh
# Cau hinh trang
st.set_page_config(
    page_title= 'Data Analysis Tool',
    layout= 'wide',
    initial_sidebar_state= 'expanded'
)

st.markdown("""
    <style>
    /* 1. Ẩn Footer và thanh trang trí màu mè */
    footer {visibility: hidden !important;}
    [data-testid="stDecoration"] {display: none !important;}

    /* 2. Ẩn các nút bên phải Header (GitHub, Deploy) */
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }

    /* 3. Ẩn menu 3 gạch nhưng KHÔNG ẩn toàn bộ Header */
    #MainMenu {
        display: none !important;
    }

    /* 4. ĐẶC BIỆT: Ép nút mở Sidebar phải hiện lên và có màu để dễ thấy */
    /* Chúng ta nhắm vào cả 2 loại ID mà Streamlit thường dùng cho nút này */
    [data-testid="stSidebarCollapsedControl"], 
    button[aria-label="Open sidebar"] {
        visibility: visible !important;
        display: flex !important;
        left: 10px !important;
        top: 10px !important;
        z-index: 1000000 !important;
        color: #FF4B4B !important; /* Màu đỏ Streamlit cho nổi bật */
    }

    /* 5. Làm trong suốt nền Header để không bị vạch trắng che nội dung */
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Neu khong co du lieu thi se o trang loading
if 'df_dulieu' not in st.session_state:
    st.session_state['df_dulieu'] = None
if 'trang_hien_tai' not in st.session_state:
        st.session_state['trang_hien_tai'] = None
if st.session_state['df_dulieu'] is None:
    cauhinh.hien_thi_man_hinh_cho()
else:
    if st.session_state['trang_hien_tai'] is None or st.session_state['trang_hien_tai'] =='trang_1':
        st.session_state['trang_hien_tai'] ='trang_1'
        cauhinh.hien_thi_dashboard()
    elif st.session_state['trang_hien_tai'] =='trang_2':
        cauhinh.trang_2()