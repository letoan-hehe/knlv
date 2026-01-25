# 🛒 Retail Sales Analysis Tool (Dành cho Cửa hàng Bán lẻ)

Đây là một ứng dụng Dashboard thông minh được xây dựng bằng **Python** và **Streamlit**, giúp các chủ cửa hàng bán lẻ nhanh chóng phân tích tình hình kinh doanh từ file dữ liệu CSV. Ứng dụng tập trung vào tính đơn giản, trực quan và tự động hóa.

## 🌟 Tính năng chính

* **Tải dữ liệu linh hoạt:** Hỗ trợ kéo thả file CSV. Hệ thống tự động xử lý và chuyển hướng đến trang Dashboard sau khi tải thành công.
* **Bộ lọc thông minh:**
    * Lọc theo thời gian (Khoảng ngày tùy chỉnh).
    * Lọc đa tầng theo **Khu vực (State)** và **Thành phố (City)**. Danh sách thành phố sẽ tự động cập nhật dựa trên khu vực được chọn.
* **Phân tích doanh số đa chiều:**
    * Biểu đồ cột phân tích doanh thu theo từng **Danh mục sản phẩm (Category)**.
    * Biểu đồ đường theo dõi xu hướng doanh thu theo thời gian (**M-Resample**).
* **Nhận diện Top/Bottom Performance:**
    * Tự động liệt kê **Top 5** sản phẩm bán chạy nhất (màu xanh).
    * Tự động liệt kê **Top 5** sản phẩm bán chậm nhất (màu đỏ) để chủ cửa hàng có kế hoạch xả kho hoặc điều chỉnh.
* **Xử lý dữ liệu tự động (Regex):** Hệ thống tự động nhận diện tên cột (Doanh số, Loại hàng, Ngày...) ngay cả khi tên cột trong file CSV bị thay đổi hoặc viết sai.

## 🛠 Công nghệ sử dụng

* **Ngôn ngữ:** Python
* **Thư viện phân tích:** Pandas, NumPy.
* **Trực quan hóa:** Matplotlib (DPI 600 cho chất lượng hình ảnh sắc nét).
* **Giao diện:** Streamlit.
* **Kỹ thuật tối ưu:** Sử dụng `@st.cache_data` để xử lý mượt mà dữ liệu lớn và Regex để tăng tính ổn định của hệ thống.

## 📂 Cấu trúc dự án

* `main.py`: Quản lý cấu hình trang và điều hướng luồng ứng dụng.
* `cauhinh.py`: Thiết kế giao diện Dashboard, các Widget lọc và bố cục biểu đồ.
* `logic.py`: Chứa toàn bộ các hàm xử lý dữ liệu, bộ lọc và các hàm vẽ biểu đồ chuyên sâu.

## 🚀 Cách chạy ứng dụng

1. Cài đặt các thư viện cần thiết:
   ```bash
   pip install streamlit pandas matplotlib