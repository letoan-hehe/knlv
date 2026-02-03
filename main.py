import streamlit as st
import pandas as pd

import cauhinh
# Cau hinh trang
st.set_page_config(
    page_title= 'Data Analysis Tool',
    layout= 'wide',
    initial_sidebar_state= 'expanded'
)

# st.markdown("""
#     <style>
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     header {visibility: hidden;}
#     </style>
#     """, unsafe_allow_html=True)

st.markdown("""
    <style>
    /* 1. Ẩn menu 3 gạch và các nút linh tinh nhưng KHÔNG ẩn header tổng */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* 2. Chỉ ẩn các phần tử hành động bên phải (GitHub, Deploy, Manage app) */
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }

    /* 3. Xử lý phần background của header để nó không che nội dung */
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
        color: transparent !important;
    }

    /* 4. Đảm bảo nút mở Sidebar (mũi tên) luôn hiển thị và có màu rõ ràng */
    button[aria-label="Open sidebar"] {
        visibility: visible !important;
        display: flex !important;
        color: #31333F !important; /* Màu đen/xám để dễ nhìn trên nền trắng */
        background-color: rgba(255, 255, 255, 0.5) !important; /* Nền mờ để không bị chìm */
        border-radius: 50%;
    }
    
    /* 5. Thu nhỏ khoảng cách phía trên cho đẹp */
    .block-container {
        padding-top: 1rem;
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