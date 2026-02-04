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
    /* 1. Ẩn thanh vạch màu trên cùng và Footer */
    [data-testid="stDecoration"], footer {display: none !important;}

    /* 2. Ẩn sạch Toolbar bên phải (nút GitHub, Deploy, 3 gạch) */
    [data-testid="stHeaderActionElements"], #MainMenu {
        display: none !important;
        visibility: hidden !important;
    }

    /* 3. Làm trong suốt Header để đẩy nội dung lên cao */
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
    }

    /* 4. HIỆN LẠI nút Sidebar (Cực kỳ quan trọng để app không bị đơ) */
    [data-testid="stSidebarCollapsedControl"], button[aria-label="Open sidebar"] {
        visibility: visible !important;
        display: flex !important;
        color: #31333F !important; /* Màu tối để dễ thấy trên nền sáng */
    }

    /* 5. Tinh chỉnh khoảng cách nội dung */
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