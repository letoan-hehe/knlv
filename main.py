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

import streamlit as st

st.markdown("""
    <style>
        /* 1. Ẩn thanh Decoration (cái vạch màu cầu vồng trên cùng) */
        [data-testid="stDecoration"] {
            display: none;
        }

        /* 2. Ẩn nút Deploy (nếu có) */
        .stDeployButton {
            display: none;
        }

        /* 3. Ẩn menu Hamburger (3 gạch) và các nút Toolbar bên phải */
        [data-testid="stToolbar"] {
            visibility: hidden !important;
        }

        /* 4. Ẩn Header nhưng vẫn giữ chỗ để nút Sidebar hoạt động */
        header {
            background-color: transparent !important;
        }

        /* 5. Ẩn Footer "Made with Streamlit" */
        footer {
            visibility: hidden !important;
        }
        
        /* 6. Tinh chỉnh nút đóng/mở Sidebar (để nó không bị ẩn theo Header) */
        /* Cái này quan trọng nếu bạn dùng Sidebar */
        [data-testid="stSidebarCollapsedControl"] {
            visibility: visible !important;
            display: block !important;
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