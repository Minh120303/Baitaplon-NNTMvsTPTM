🌿 PHÂN TÍCH DỮ LIỆU HÌNH ẢNH LÁ CÂY ĐỂ PHÁT HIỆN BỆNH CÂY

📝 Giới thiệu:

Đề tài nghiên cứu ứng dụng trí tuệ nhân tạo (AI) và xử lý ảnh để phát hiện sớm các bệnh thường gặp trên lá cây. Hệ thống hỗ trợ người nông dân phát hiện bệnh chính xác, nhanh chóng, góp phần tăng năng suất cây trồng và thúc đẩy phát triển nông nghiệp thông minh.

🧠 Chức năng chính:

Chức năng Mô tả
Thu thập dữ liệu hình ảnh Sử dụng camera chụp ảnh lá cây có triệu chứng bệnh.
Xử lý ảnh và trích xuất đặc trưng Dùng OpenCV xử lý ảnh, loại nhiễu, trích xuất đặc điểm (đốm, màu, hình dạng).
Nhận diện bệnh cây bằng AI Áp dụng mô hình học sâu (CNN) để phân loại loại bệnh từ ảnh đầu vào.
Giao diện người dùng Web app cho phép tải ảnh, hiển thị kết quả và gợi ý cách xử lý bệnh.
Lưu trữ và phân tích dữ liệu Dữ liệu ảnh và kết quả được lưu trữ phục vụ thống kê, giám sát lâu dài.

⚙️ Công nghệ sử dụng:

Thành phần Mô tả
Python + Flask Xây dựng backend web và xử lý logic chương trình.
OpenCV Tiền xử lý hình ảnh (lọc nhiễu, resize, chuẩn hóa màu sắc).
TensorFlow/Keras Huấn luyện và triển khai mô hình CNN nhận dạng bệnh lá.
Cơ sở dữ liệu MongoDB Lưu trữ ảnh, kết quả phân tích, thời gian và gợi ý xử lý.
Dataset PlantVillage Bộ dữ liệu chuẩn gồm 38 lớp bệnh lá với ~54.000 ảnh.

🔄 Chu trình hoạt động:
 1. Người dùng tải ảnh lên hệ thống.
 2. Hệ thống xử lý ảnh: chuẩn hóa kích thước, tăng cường chất lượng.
 3. Phân tích bằng AI: nhận diện loại bệnh (hoặc xác định lá khỏe mạnh).
 4. Hiển thị kết quả và gợi ý xử lý.
 5. Lưu dữ liệu: lưu ảnh, thời gian, kết quả chẩn đoán.

📊 Kết quả thử nghiệm:
 • Tập dữ liệu: ~54.000 ảnh (38 lớp).
 • Huấn luyện: 70% train, 30% validation, 14 epoch.
 • Kết quả mô hình: Độ chính xác 90%, loss ~33%.


 
![image](https://github.com/user-attachments/assets/5d7b2df5-63a0-4476-97ff-3b8c48329852)         














![image](https://github.com/user-attachments/assets/1a8d5c51-4380-49a8-990c-107eaaf97d89)










![image](https://github.com/user-attachments/assets/90e892d0-0743-436e-a335-0172ec546d60)












![image](https://github.com/user-attachments/assets/f6a5fec1-c08a-4c58-af96-b83d699adadb)              ![image](https://github.com/user-attachments/assets/22931622-839a-42e5-a476-67347a61a116)















🚀 Mục tiêu mở rộng:
 • Tăng kích thước và tính đa dạng của tập dữ liệu thực tế.
 • Phát triển ứng dụng điện thoại tích hợp camera.
 • Cảnh báo sớm khi bệnh có dấu hiệu lây lan.
 • Gợi ý cách xử lý bằng thuốc phù hợp.
 • Tích hợp với drone hoặc cảm biến IoT để giám sát quy mô lớn.


👨‍💻 Tác giả Họ tên: Lê Thị Minh 
