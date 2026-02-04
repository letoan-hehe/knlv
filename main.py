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
    /* 1. Ẩn cụm nút bên phải (GitHub, Deploy) */
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }

    /* 2. Ẩn menu 3 gạch */
    #MainMenu {
        display: none !important;
    }

    /* 3. LÀM NỔI BẬT nút mở Sidebar (Nằm bên trái) */
    /* Chúng ta KHÔNG ẩn Header, chỉ làm nó trong suốt để nút này lộ ra */
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
    }

    [data-testid="stSidebarCollapsedControl"] {
        background-color: #FF4B4B !important; /* Màu đỏ cho dễ thấy */
        color: white !important;
        border-radius: 50%;
        visibility: visible !important;
        display: flex !important;
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