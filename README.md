# Hana - Dự án Trợ lý Giọng nói Đầu tiên của tôi

Chào mừng bạn đến với kho lưu trữ của **Hana**, dự án trợ lý giọng nói đầu tiên của tôi! Dự án này thể hiện một trợ lý giọng nói cơ bản có khả năng phản hồi các yêu cầu và truy vấn được cài đặt sẵn. Hana được thiết kế để trở thành một giới thiệu đơn giản nhưng đầy đủ chức năng về lập trình tương tác bằng giọng nói.

## Về Hana

Hana là một trợ lý giọng nói hoạt động dựa trên các lệnh, có khả năng:
* **Phản hồi các yêu cầu được cài đặt sẵn:** Hana được lập trình để nhận diện và trả lời các câu hỏi hoặc lệnh cụ thể.
* **Thực hiện các chức năng tiện ích cơ bản:** (Dựa trên tên file của bạn, gợi ý các khả năng này)
    * Thông báo **thời gian** hiện tại (`function/thoi_gian.py`).
    * Thông báo **ngày tháng** hiện tại (`function/ngay_thang.py`).
    * Cung cấp thông tin **thời tiết** (`function/thoi_tiet.py`).
    * **Mở ứng dụng** (`function/mo_ung_dung.py`).
    * Thực hiện các tác vụ **tìm kiếm** cơ bản (`function/tim_kiem.py`).
    * Xử lý các chức năng **nói** (`function/noi.py`) và **nghe** (`function/nghe.py`).
    * Kiểm tra **kết nối mạng** (`function/kiem_tra_mang.py`).
    * Bao gồm "detect_hana.py" (có thể dùng để phát hiện từ khóa đánh thức hoặc tương tác ban đầu).
    * Có khả năng đọc các **bảng số đếm** từ file (`bang_so_dem.txt`).

Dự án này tập trung vào logic cốt lõi của việc xử lý đầu vào giọng nói, nhận dạng lệnh và đưa ra các phản hồi đã được lập trình.

## Bắt đầu

Để chạy Hana trên máy tính cục bộ của bạn, hãy làm theo các bước đơn giản sau:

### Yêu cầu cài đặt

Bạn cần cài đặt Python trên hệ thống của mình.
Dự án này yêu cầu một số thư viện Python cụ thể.

### 1. Cài đặt giọng nói tiếng Việt trên Windows

Để Hana có thể nói tiếng Việt trên hệ điều hành Windows, bạn cần thêm thông tin về giọng nói "Microsoft An - Vietnamese (Vietnam)" vào Registry.

1.  **Tải xuống file `an-vi.reg`:**
    * File này nằm sẵn trong kho lưu trữ của dự án.

2.  **Chạy file `.reg`:**
    * Tìm file `an-vi.reg` trong thư mục gốc của dự án.
    * Nhấp đúp chuột vào file `an-vi.reg`.
    * Một cửa sổ xác nhận sẽ xuất hiện, hỏi bạn có muốn thêm thông tin này vào Registry hay không. Chọn **"Yes" (Có)** để tiếp tục.
    * Sau khi hoàn tất, bạn sẽ nhận được thông báo rằng các khóa đã được thêm vào Registry thành công.

*(Lưu ý: Thao tác này sẽ thêm giọng nói Microsoft An vào hệ thống của bạn, cho phép các ứng dụng TTS (Text-to-Speech) sử dụng giọng nói tiếng Việt.)*

### 2. Cài đặt và chạy dự án

1.  **Clone kho lưu trữ:**
    ```bash
    git clone https://github.com/VNthcong520712/Hana.git
    cd Hana
    ```

2.  **Tạo và kích hoạt môi trường ảo:**
    Rất khuyến nghị sử dụng môi trường ảo để quản lý các thư viện phụ thuộc.
    ```bash
    python -m venv venv
    # Trên Windows:
    .\venv\Scripts\activate
    # Trên macOS/Linux: (Lưu ý: Giọng nói tiếng Việt chỉ hỗ trợ trên Windows với phương pháp này)
    # source venv/bin/activate
    ```

3.  **Cài đặt các thư viện phụ thuộc:**
    Dự án này cần các thư viện sau. Hãy chạy lệnh:
    ```bash
    pip install -r requirements.txt
    ```
    *(Nếu bạn gặp lỗi `ModuleNotFoundError`, hãy kiểm tra lại file `requirements.txt` và cài đặt các thư viện bị thiếu.)*

### 3. Chạy Hana

Để khởi động Hana, bạn cần chạy tệp server chính:

```bash
python server.py
