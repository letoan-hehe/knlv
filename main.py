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
    /* 1. Ẩn menu chính (3 gạch) và các nút Toolbar (GitHub, Deploy) */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 2. Ẩn nút "Manage app" và các icon phía góc phải */
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }

    /* 3. HIỆN LẠI nút mở Sidebar (quan trọng) */
    /* Streamlit thay đổi class này liên tục, chúng ta nhắm vào nút có aria-label */
    button[aria-label="Open sidebar"] {
        visibility: visible !important;
        display: flex !important;
        position: fixed;
        top: 10px;
        left: 10px;
        z-index: 999999;
        color: #31333F; /* Hoặc màu tùy chọn để dễ thấy */
    }

    /* 4. Ẩn footer 'Made with Streamlit' */
    footer {visibility: hidden;}
    
    /* 5. Loại bỏ khoảng trắng dư thừa do header bị ẩn */
    .block-container {
        padding-top: 2rem;
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