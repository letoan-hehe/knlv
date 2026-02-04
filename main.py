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
    /* 1. Ẩn toàn bộ thanh Header (chứa nút GitHub và Source) */
    header[data-testid="stHeader"] {
        visibility: hidden !important;
        height: 0 !important;
    }

    /* 2. Ẩn Footer và vạch màu trang trí */
    footer {visibility: hidden !important;}
    [data-testid="stDecoration"] {display: none !important;}

    /* 3. Lôi nút mở Sidebar ra ngoài và ép nó phải hiện */
    /* Chúng ta đặt nó cố định ở góc trái màn hình */
    [data-testid="stSidebarCollapsedControl"] {
        visibility: visible !important;
        display: flex !important;
        position: fixed !important;
        top: 15px !important;
        left: 15px !important;
        z-index: 999999 !important;
        background-color: #f0f2f6 !important;
        border: 1px solid #d1d5db !important;
        border-radius: 4px !important;
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