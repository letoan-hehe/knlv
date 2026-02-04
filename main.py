import streamlit as st
import pandas as pd

import cauhinh
# Cau hinh trang
st.set_page_config(
    page_title= 'Data Analysis Tool',
    layout= 'wide',
    initial_sidebar_state= 'auto'
)

st.markdown("""
    <style>
    /* 1. Ẩn thanh vạch màu và Footer */
    [data-testid="stDecoration"], footer {display: none !important;}

    /* 2. KHÔNG ẩn header, mà ẩn nội dung bên phải của nó */
    /* Cách này giúp nút Sidebar (nằm bên trái) không bị ảnh hưởng */
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }
    
    /* Ẩn menu 3 gạch */
    #MainMenu {
        display: none !important;
    }

    /* 3. Làm trong suốt nền Header để không bị vạch trắng che biểu đồ */
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
    }

    /* 4. ÉP nút mở Sidebar phải hiện lên với màu sắc nổi bật */
    /* Nếu nó vẫn ẩn, ta dùng position fixed để đưa nó ra khỏi header */
    [data-testid="stSidebarCollapsedControl"] {
        visibility: visible !important;
        display: flex !important;
        background-color: #f0f2f6 !important; /* Màu nền nhẹ cho nút */
        border-radius: 0 10px 10px 0 !important;
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