# HƯỚNG DẪN DÀNH CHO MÁY CON (CHỈ NHẬN ĐỒNG BỘ - READ-ONLY)

Tài liệu này hướng dẫn cài đặt trên các máy tính khác để nhận dữ liệu đồng bộ liên tục theo thời gian thực từ máy chủ (Master), với quyền **chỉ đọc (không thể sửa hoặc ghi đè lên máy chủ)** và **tự động chạy ngầm mỗi khi khởi động lại máy tính**.

---

### Bước 1: Clone repository về máy con (Chỉ làm 1 lần duy nhất)
Mở PowerShell trên máy con và gõ lệnh:
```powershell
git clone https://github.com/minhducectminhhoaect-commits/antigravity-project-3.git
cd antigravity-project-3
```

---

### Bước 2: Kích hoạt tự động đồng bộ cùng khởi động Windows

Vào thư mục `client_sync` trong thư mục vừa tải về:
> **Chỉ cần nhấp đúp chuột vào tệp: `cai_dat_khoi_dong_cung_windows.bat`**

Sau khi chạy:
- Hệ thống sẽ tự động thêm tiến trình vào danh sách **Startup của Windows**.
- Từ thời điểm này trở đi, **mỗi khi máy tính khởi động lại hoặc đăng nhập**, tiến trình đồng bộ sẽ tự chạy ngầm.
- Người dùng không cần phải click hay mở bất kỳ cửa sổ nào thủ công nữa.

---

### Danh sách các công cụ trong thư mục `client_sync`:

| Tên tệp | Chức năng |
| :--- | :--- |
| `cai_dat_khoi_dong_cung_windows.bat` | **Cài đặt tự khởi động cùng Windows** và bật đồng bộ ngầm ngay lập tức |
| `go_khoi_dong_cung_windows.bat` | Hủy tính năng tự khởi động cùng Windows |
| `start_client_sync.bat` | Chạy đồng bộ có cửa sổ đen hiển thị thông báo tiến trình |
| `start_client_sync_background.vbs` | Chạy đồng bộ ngầm thủ công cho phiên hiện tại |
| `stop_client_sync.bat` | Tắt tiến trình đồng bộ đang chạy ngầm |
| `client_sync.log` | Nhật ký lưu lại các lần nhận file cập nhật từ máy chủ |

---

### Cơ chế bảo vệ dữ liệu (Chỉ xem - Không sửa):
1. **Bảo vệ từ GitHub:** Máy con không có quyền `Write/Push`. Nếu người dùng ở máy con cố tình push lên GitHub, GitHub sẽ lập tức chặn lại.
2. **Bảo vệ từ Script nội bộ:** Khi phát hiện máy chủ có cập nhật mới, script sẽ tự động khôi phục dữ liệu về đúng bản gốc (`git reset --hard origin/main`). Mọi thao tác sửa đổi vô ý của người dùng trên máy con sẽ tự động bị xóa bỏ để luôn khớp 100% với máy chủ.
