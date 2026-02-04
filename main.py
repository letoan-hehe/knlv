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
    /* Ẩn thanh trang trí cầu vồng ở trên cùng */
    [data-testid="stDecoration"] {display: none !important;}

    /* Ẩn nút Deploy, nút GitHub và Menu 3 gạch */
    header[data-testid="stHeader"] [data-testid="stHeaderActionElements"], 
    #MainMenu {
        display: none !important;
        visibility: hidden !important;
    }

    /* Quan trọng: Vẫn phải giữ Header nhưng làm trong suốt để NÚT SIDEBAR không bị mất */
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
        color: transparent !important;
    }

    /* Đảm bảo nút mở Sidebar luôn hiện rõ để người dùng bấm được */
    button[aria-label="Open sidebar"] {
        visibility: visible !important;
        display: flex !important;
        color: #31333F !important; /* Đổi màu nút để nó không bị trong suốt theo header */
    }

    /* Ẩn Footer 'Made with Streamlit' */
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