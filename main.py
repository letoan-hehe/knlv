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
    /* 1. Nhắm thẳng vào cụm Toolbar bên phải của Header */
    header div[data-testid="stHeaderActionElements"], 
    header .stAppDeployButton,
    [data-testid="stToolbar"] {
        display: none !important;
    }

    /* 2. Ẩn menu 3 gạch bằng cách tìm nút có aria-expanded */
    button[aria-label="Manage app"], 
    button[id="MainMenu"] {
        display: none !important;
    }

    /* 3. QUAN TRỌNG: Hiện lại nút Sidebar nhưng dời nó ra khỏi Header */
    /* Nếu ẩn header mà không dời nút này, nó sẽ bị mất tương tác */
    [data-testid="stSidebarCollapsedControl"] {
        background-color: #f0f2f6;
        border-radius: 0 10px 10px 0;
        left: 0;
        position: fixed;
        z-index: 1000001;
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