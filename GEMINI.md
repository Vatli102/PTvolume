# QUY TẮC & TIÊU CHUẨN THIẾT KẾ WEBSITE PTVOLUME.COM

Tài liệu này ghi nhớ toàn bộ các tiêu chuẩn bắt buộc cho mọi trang web, bài viết blog và tài liệu được phát triển cho website **PTvolume.com**:

---

### 1. BẢO VỆ BẢN QUYỀN & CHỐNG SAO CHÉP (Anti-Copy Protection)
* **Chặn bôi đen nội dung:** Áp dụng CSS `user-select: none; -webkit-user-select: none;` cho toàn bộ nội dung bài viết và phân tích.
* **Chặn chuột phải:** Vô hiệu hóa menu chuột phải (`oncontextmenu="return false;"`).
* **Chặn phím tắt:** Chặn các tổ hợp phím sao chép (`Ctrl+C`, `Ctrl+U`, `Ctrl+S`, `F12`, `Ctrl+Shift+I`) và hiển thị thông báo bản quyền trang nhã khi người dùng cố sao chép.

---

### 2. ĐÓNG DẤU BẢN QUYỀN HÌNH ẢNH (Image Watermark: PTvolume.com)
* Mọi hình ảnh phân tích kỹ thuật, biểu đồ, ảnh bìa bài viết đều phải có lớp bọc watermark (`.watermark-container`).
* Watermark hiển thị chữ mờ `PTvolume.com` ở góc dưới bên phải với nền mờ bán trong suốt, kèm biểu tượng thương hiệu.
* Vô hiệu hóa tính năng kéo thả ảnh (`draggable="false"`) và ngăn tải trực tiếp.

---

### 3. TÍNH NĂNG BÌNH LUẬN CHO ĐỘC GIẢ (Interactive Comments)
* Mọi bài viết phân tích / blog đều phải tích hợp khung bình luận (Comments Section) gồm:
  - Form nhập Họ tên, Nội dung bình luận, Đánh giá thảo luận.
  - Hiển thị danh sách bình luận cộng đồng theo thời gian thực (hỗ trợ lưu trữ tương tác hoặc tích hợp Giscus/Utterances/Disqus).
  - Khuyến khích trader trao đổi góc nhìn đa chiều về nến, Volume và bẫy giá Smart Money.

---

### 4. NHẬN DIỆN THƯƠNG HIỆU & PHÁP LÝ
* Logo: Báo đen `PT VOLUME - MARKET ANALYSIS` (`logo.jpg`).
* Tone màu: Dark Theme chuyên nghiệp (`#0B0E14`, xanh `#2962FF`, xanh cyan `#00E5FF`, vàng `#F0B90B`).
* Luôn giữ liên kết 5 trang cốt lõi: Giới thiệu, Liên hệ, Điều khoản, Bảo mật, Cảnh báo rủi ro.
