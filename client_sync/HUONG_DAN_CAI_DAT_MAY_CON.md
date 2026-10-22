# HƯỚNG DẪN DÀNH CHO MÁY CON (CHỈ NHẬN ĐỒNG BỘ - READ-ONLY)

Tài liệu này hướng dẫn cài đặt trên các máy tính khác để nhận dữ liệu đồng bộ liên tục theo thời gian thực từ máy chủ (Master), với quyền **chỉ đọc (không thể sửa hoặc ghi đè lên máy chủ)**.

---

### Bước 1: Clone repository về máy con
Mở PowerShell / Terminal trên máy con và gõ lệnh:
```powershell
git clone https://github.com/minhducectminhhoaect-commits/antigravity-project-3.git
cd antigravity-project-3
```

---

### Bước 2: Bật chế độ tự động nhận đồng bộ liên tục
Truy cập vào thư mục `client_sync` trong thư mục vừa clone:
- **Cách 1 (Chạy xem tiến trình trực tiếp):** Nhấp đúp vào `start_client_sync.bat`. Cửa sổ sẽ báo mỗi khi có bản cập nhật mới từ máy chủ.
- **Cách 2 (Chạy ngầm hoàn toàn):** Nhấp đúp vào `start_client_sync_background.vbs`. Tiến trình sẽ chạy ngầm không hiện cửa sổ.

---

### Cơ chế bảo vệ chống sửa đổi (Read-Only):
1. **Quyền trên GitHub:** Các máy con mặc định không có quyền `write/push` lên GitHub, do đó họ không thể làm thay đổi dữ liệu gốc trên GitHub.
2. **Tự động khôi phục (`git reset --hard`):** Nếu người dùng tại máy con lỡ tay sửa, tạo file rác hoặc xóa nhầm file trong thư mục của họ, script ở máy con sẽ tự động phát hiện và khôi phục lại 100% nguyên trạng như máy chủ gốc.
