# 🛒 Retail Sales Analysis Tool 

Retail Sales Analysis Tool là một ứng dụng Dashboard chuyên sâu được phát triển bằng Python và Streamlit. Công cụ này giúp các nhà quản lý và chủ cửa hàng bán lẻ biến các file dữ liệu CSV thô thành những thông tin chi tiết (insights) về doanh thu, lợi nhuận và hiệu suất sản phẩm chỉ trong vài giây.

## 🌟 Tính năng chính

### 1. Quản lý dữ liệu linh hoạt

- **Hỗ trợ đa nguồn**: Cho phép tải file CSV trực tiếp hoặc sử dụng Dữ liệu mẫu (15 dòng) tích hợp sẵn để trải nghiệm nhanh các tính năng.
- **Kiểm tra tính hợp lệ**: Tự động kiểm tra các cột bắt buộc như: Ngày đặt hàng, Sản phẩm, Doanh thu, Lợi nhuận, Khu vực, Tỉnh....
- **Xử lý thông minh**: Tự động làm sạch tên cột (strip spaces) và nhận diện định dạng ngày tháng tiếng Việt.

### 2. Dashboard Tổng quan (Trang 1)

- **Hệ thống KPI Cards**: Theo dõi 3 chỉ số sinh tử: Tổng doanh thu, Tổng lợi nhuận và Tổng số đơn hàng.
- **So sánh tăng trưởng (Delta)**: Tự động tính toán và hiển thị % tăng trưởng so với tháng trước đó, giúp nhận diện xu hướng kinh doanh ngay lập tức.
- **Phân tích Top/Bottom**:
  - Top 5 sản phẩm bán chạy: Hiển thị với sắc xanh (Greens) tượng trưng cho hiệu suất tốt.
  - Top 5 sản phẩm bán kém: Hiển thị với sắc đỏ (Reds) để cảnh báo về tồn kho hoặc sản phẩm lỗi thời.
- **Xu hướng thời gian**: Biểu đồ đường (Line Chart) theo dõi biến động doanh số theo từng tháng.

### 3. Phân tích Tùy chỉnh (Trang 2)

- **Self-Service BI**: Người dùng có quyền tự chọn Trục X (Cột phân loại) và Trục Y (Chỉ số số học) để tạo biểu đồ theo ý muốn.
- **Đa dạng phép toán**: Hỗ trợ Tổng (Sum), Trung bình (Mean), Lớn nhất (Max), Nhỏ nhất (Min) và Đếm (Count).
- **Linh hoạt loại hình**: Chuyển đổi giữa biểu đồ Cột đứng, Đường và biểu đồ Tròn (Donut chart).

## 📂 Cấu trúc dự án

```
retail-sales-analysis-tool/
├── main.py       # Điểm khởi đầu của ứng dụng
├── cauhinh.py    # Giao diện người dùng (UI)
├── logic.py      # Xử lý dữ liệu và vẽ biểu đồ
└── README.md     # Tài liệu hướng dẫn
```

- **main.py**: Điểm khởi đầu của ứng dụng. Quản lý cấu hình trang (set_page_config), khởi tạo session_state và điều phối luồng giữa màn hình chờ và các trang dashboard.
- **cauhinh.py**: Chứa toàn bộ giao diện người dùng (UI). Định nghĩa cấu trúc các cột, widget lọc, các hàm hiển thị Metric và bố cục của Trang 1 & Trang 2.
- **logic.py**: Thư viện chứa các hàm xử lý dữ liệu và vẽ biểu đồ. Bao gồm các hàm lọc dữ liệu (filter_data), định dạng tiền tệ thông minh (smart_format) và các hàm Matplotlib tùy biến.

## 🛠 Công nghệ sử dụng

- **Ngôn ngữ**: Python 3.x
- **Thư viện Dashboard**: Streamlit
- **Xử lý dữ liệu**: Pandas
- **Trực quan hóa**: Matplotlib (Tối ưu hiển thị với định dạng số rút gọn K, M, B)

## 🚀 Hướng dẫn cài đặt và sử dụng

### 1. Cài đặt môi trường

Yêu cầu Python đã được cài đặt. Chạy lệnh sau để cài đặt các thư viện bổ trợ:

```bash
pip install streamlit pandas matplotlib
```

### 2. Khởi chạy ứng dụng

Di chuyển vào thư mục dự án và chạy:

```bash
streamlit run main.py
```

### 3. Chuẩn bị dữ liệu CSV

Để Dashboard hoạt động đầy đủ tính năng, file CSV của bạn nên có các tiêu đề cột sau:

| Cột | Mô tả |
|-----|-------|
| Ngày đặt hàng | Định dạng ngày (DD/MM/YYYY) |
| Sản phẩm | Tên mặt hàng |
| Doanh thu | Giá trị số |
| Lợi nhuận | Giá trị số |
| Khu vực | Miền Bắc, Miền Trung, Miền Nam... |
| Tỉnh | Tên tỉnh/thành phố |

## 💡 Lưu ý vận hành

- Hệ thống sẽ tự động **Reset các bộ lọc** (Ngày, Khu vực, Tỉnh) mỗi khi bạn tải một file dữ liệu mới để đảm bảo tính chính xác của biểu đồ.
- Nếu file tải lên thiếu các cột chuẩn, ứng dụng sẽ đưa ra cảnh báo nhưng bạn vẫn có thể sử dụng Trang 2 để phân tích các cột dữ liệu hiện có.

---

**Phát triển bởi**: Fruits Team  
