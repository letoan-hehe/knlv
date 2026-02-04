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
    /* 1. Ẩn nút Fullscreen trên các biểu đồ và bảng để ngăn lộ source */
    [data-testid="StyledFullScreenButton"] {
        display: none !important;
    }

    /* 2. Ẩn Toolbar và các nút Action Elements */
    [data-testid="stHeaderActionElements"], #MainMenu {
        display: none !important;
    }

    /* 3. Giữ nút Sidebar luôn hiện rõ ở vị trí cố định */
    [data-testid="stSidebarCollapsedControl"] {
        display: flex !important;
        visibility: visible !important;
        position: fixed !important;
        top: 10px !important;
        left: 10px !important;
        z-index: 999999 !important;
    }

    /* 4. Ẩn Footer */
    footer {visibility: hidden !important;}
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