import streamlit as st
import pandas as pd

import cauhinh
# Cau hinh trang
st.set_page_config(
    page_title= 'Data Analysis Tool',
    layout= 'wide'
)

st.markdown("""
    <style>
    /* 1. Ẩn Footer và vạch màu trang trí phía trên cùng */
    footer {visibility: hidden !important;}
    [data-testid="stDecoration"] {display: none !important;}

    /* 2. CHỈ ẩn cụm nút bên phải (GitHub, Deploy, 3 gạch) */
    /* Chúng ta nhắm vào container chứa các nút này */
    [data-testid="stHeaderActionElements"], 
    header button[aria-label="Manage app"],
    header button[id="MainMenu"] {
        display: none !important;
    }

    /* 3. LÀM TRONG SUỐT Header để nó không che biểu đồ */
    /* Nhưng vẫn phải để nó 'tồn tại' để nút Sidebar (bên trái) có chỗ bám */
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
        border: none !important;
    }

    /* 4. ĐẢM BẢO nút Sidebar luôn hiện rõ và có thể bấm được */
    [data-testid="stSidebarCollapsedControl"] {
        visibility: visible !important;
        display: flex !important;
        color: #31333F !important; /* Màu tối để nổi bật trên nền trắng */
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