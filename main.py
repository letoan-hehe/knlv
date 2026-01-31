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
    /* 1. Ẩn menu 3 gạch và nút GitHub/Deploy */
    #MainMenu {visibility: hidden;}
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0); /* Làm trong suốt header */
        height: 0px; /* Thu nhỏ độ cao để không đè lên nội dung */
    }
    
    /* 2. Ẩn các icon bên phải của header nhưng GIỮ lại vùng chứa nút bên trái */
    [data-testid="stHeaderActionElements"] {
        visibility: hidden;
    }

    /* 3. ĐÂY LÀ PHẦN QUAN TRỌNG: Cấu hình cho nút hiện lại sidebar */
    /* Khi sidebar đóng, nút này nằm trong một div riêng, ta phải ép nó hiện lên */
    [data-testid="sidebar-collapsed-control"] {
        visibility: visible !important;
        display: flex !important;
        top: 10px; /* Điều chỉnh vị trí nút để không bị lệch */
    }

    /* 4. Ẩn footer */
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