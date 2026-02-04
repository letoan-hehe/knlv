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
    /* Ẩn các nút bên phải và menu 3 gạch */
    [data-testid="stHeaderActionElements"], #MainMenu {
        display: none !important;
    }

    /* Giữ header trong suốt để nút mở Sidebar (bên trái) có chỗ đứng */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
    }

    /* Đảm bảo nút Sidebar luôn hiện rõ */
    [data-testid="stSidebarCollapsedControl"] {
        visibility: visible !important;
        display: flex !important;
        color: #FF4B4B !important;
    }
    
    footer {visibility: hidden;}
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