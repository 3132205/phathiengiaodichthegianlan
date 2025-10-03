# phathiengiaodichthegianlan

 Hệ thống dự đoán giao dịch thẻ tín dụng (Credit Card Fraud Detection)

 Giới thiệu

Trong thời đại công nghệ số, việc thanh toán qua thẻ tín dụng ngày càng phổ biến. Tuy nhiên, song song với sự tiện lợi đó, các hoạt động **gian lận thẻ tín dụng (credit card fraud)** cũng gia tăng nhanh chóng và trở thành thách thức lớn đối với các ngân hàng và tổ chức tài chính.

Mục tiêu của dự án này là xây dựng một **hệ thống phát hiện gian lận thẻ tín dụng** dựa trên **Machine Learning**. Thông qua việc huấn luyện mô hình trên tập dữ liệu chứa các đặc trưng giao dịch, hệ thống có khả năng dự đoán một giao dịch là **hợp lệ (0)** hay **gian lận (1)**.

Ngoài mô hình, nhóm còn phát triển một ứng dụng web bằng **Flask** cho phép người dùng nhập dữ liệu hoặc tải lên file Excel/CSV để nhận kết quả dự đoán ngay lập tức.

---

 Cấu trúc dự án

```
 credit-card-fraud-detection
│──  static/              # Chứa CSS, JS, hình ảnh minh họa
│──  templates/           # Giao diện HTML (Flask render_template)
│   │── index.html          # Trang giao diện chính
│── app.py                  # Flask web app
│── model.pkl               # Model Machine Learning đã huấn luyện
│── scaler.pkl              # StandardScaler dùng để chuẩn hóa dữ liệu
│── train_model.py          # Script huấn luyện mô hình
│── requirements.txt        # Danh sách thư viện cần thiết
│── README.md               # Tài liệu hướng dẫn sử dụng
```

---

 Cài đặt và chạy thử

1. Clone repo

```bash
git clone https://github.com/<your-username>/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```

### 2. Tạo môi trường ảo và cài thư viện

```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
```

### 3. Huấn luyện và lưu mô hình

```bash
python train_model.py
```

Sau khi chạy xong, sẽ sinh ra file `model.pkl` và `scaler.pkl` để sử dụng cho ứng dụng web.

### 4. Chạy ứng dụng web

```bash
python app.py
```

Mở trình duyệt và truy cập: `http://127.0.0.1:5000/`

---

 Mô hình Machine Learning

Trong dự án, nhóm tiến hành thử nghiệm nhiều thuật toán khác nhau:

* **Logistic Regression**: đơn giản, nhanh, dễ triển khai nhưng độ chính xác chưa cao.
* **Random Forest**: cho kết quả ổn định, giảm hiện tượng overfitting.
* **XGBoost**: thuật toán mạnh mẽ, xử lý tốt dữ liệu mất cân bằng và thường đạt hiệu suất cao.

### Quy trình:

1. **Tiền xử lý dữ liệu**:

   * Chuẩn hóa dữ liệu bằng `StandardScaler`
   * Chia dữ liệu thành tập huấn luyện và kiểm thử theo tỷ lệ 80:20
   * Giải quyết vấn đề mất cân bằng dữ liệu

2. **Huấn luyện mô hình**

   * Lần lượt huấn luyện Logistic Regression, Random Forest, XGBoost
   * So sánh kết quả qua các chỉ số: `Accuracy, Precision, Recall, F1-score`

3. **Lưu mô hình**

   * Mô hình tốt nhất sẽ được lưu lại dưới dạng `.pkl`

---

 Kết quả và đánh giá

Trong quá trình thử nghiệm:

* **Random Forest** và **XGBoost** đạt hiệu quả cao hơn Logistic Regression
* Chỉ số **Recall** được ưu tiên hơn Accuracy, vì trong thực tế cần hạn chế bỏ sót các giao dịch gian lận.
* Biểu đồ so sánh các chỉ số cho thấy XGBoost có hiệu suất tổng thể tốt nhất.

Ứng dụng web hiển thị kết quả dự đoán theo 2 nhãn:

* `0` → **Hợp lệ**
* `1` → **Gian lận**

Ngoài ra, người dùng có thể tải file Excel/CSV để dự đoán hàng loạt.

---

 Giao diện ứng dụng

* Giao diện được thiết kế bằng **HTML + CSS + Bootstrap**
* Hỗ trợ nhập dữ liệu thủ công hoặc tải lên file
* Hiển thị kết quả dưới dạng văn bản và có thể mở rộng thêm biểu đồ

Ví dụ minh họa:

<img width="1009" height="501" alt="Image" src="https://github.com/user-attachments/assets/a0260c92-3469-4f42-baa1-529dcd57b700" />

<img width="1009" height="255" alt="Image" src="https://github.com/user-attachments/assets/ab9c8af3-bf7e-4a75-96a1-312c126eb327" />

<img width="1009" height="519" alt="Image" src="https://github.com/user-attachments/assets/9d2b3efa-8acd-4f3b-a5f7-628eb5abc8d7" />

<img width="1009" height="501" alt="Image" src="https://github.com/user-attachments/assets/6ab365a3-8e67-4025-a808-b3472f34f224" />

---

 Ưu điểm

* Tích hợp nhiều mô hình và so sánh hiệu quả
* Ứng dụng web trực quan, dễ sử dụng cho cả người không chuyên
* Cho phép dự đoán cả từng giao dịch lẫn hàng loạt giao dịch

 Nhược điểm

* Dữ liệu gốc bị mất cân bằng (giao dịch gian lận rất ít) → mô hình có thể bị lệch nếu không xử lý tốt
* Web còn đơn giản, chưa có tính năng quản lý tài khoản người dùng
* Mới chạy thử nghiệm trên dữ liệu sẵn có, chưa triển khai trên dữ liệu thực tế

 Hướng phát triển

* Nâng cấp giao diện web thân thiện và chuyên nghiệp hơn (thêm dashboard, biểu đồ, thống kê)
* Tích hợp thêm các kỹ thuật Deep Learning (LSTM, Autoencoder) để cải thiện khả năng phát hiện gian lận
* Triển khai mô hình lên **Cloud (Heroku, AWS, GCP)** để dễ dàng truy cập từ bất kỳ đâu
* Xây dựng hệ thống cảnh báo thời gian thực cho ngân hàng/tổ chức tài chính

