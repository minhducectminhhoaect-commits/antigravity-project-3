# Quy Chuẩn Kỹ Thuật CAD Automation (AutoCAD Engineering Rules)

Khi nhận các tác vụ liên quan đến thiết kế, vẽ kỹ thuật hoặc lập trình cho AutoCAD:

## 1. Đơn Vị & Không Gian
- Mọi bản vẽ mặc định dựng ở tỷ lệ **1:1** trong không gian **Model Space**, đơn vị tuyệt đối là **Milimét (mm)**.
- Khi nhận dữ liệu đầu vào (từ text prompt hoặc ảnh phác thảo), phải lập bảng ma trận tọa độ lưới trục trước khi phát sinh lệnh vẽ.

## 2. Tiêu Chuẩn Quản Lý Layer
- Tuyệt đối không vẽ mọi thứ trên layer `0` hoặc layer `Defpoints`.
- Mọi đối tượng phải được gán đúng Layer chức năng:
  - `0_GRID`: Tim trục (Màu 1/8, Center)
  - `0_COLUMN`: Cột kết cấu (Màu 4/2, Continuous)
  - `0_WALL_EXT`: Tường bao ngoài (Màu 3/7, Continuous)
  - `0_WALL_INT`: Tường ngăn phòng (Màu 2, Continuous)
  - `0_OPENINGS`: Cửa đi, cửa sổ (Màu 4, Continuous)
  - `0_DIM`: Đường kích thước (Màu 7/Black, Continuous)
  - `0_TEXT`: Chữ ghi chú, tên phòng (Màu 7/Black, Continuous)

## 3. Tiêu Chuẩn Mã AutoLISP
- Luôn bọc mã trong hàm có bẫy lỗi `*error*` để phục hồi `OSMODE` và `CMDECHO`.
- Luôn khai báo biến cục bộ (Local variables) để tránh ô nhiễm bộ nhớ AutoCAD.
- Luôn tắt `OSMODE` (`(setvar "OSMODE" 0)`) trong quá trình vẽ tự động để tọa độ không bị nhảy lệch do bắt điểm tự động.
- Khi viết cho AutoCAD LT: Tuyệt đối không dùng thư viện Visual LISP / ActiveX (`vlax-*`, `vla-*`).

## 4. Kiểm Soát Màu Sắc & Xuất Bản Vẽ (Plotting)
- Màu ACI 7 (White/Black) hiển thị là màu trắng trên nền Model đen của CAD, nhưng khi xuất PDF nền giấy trắng sẽ bị tàng hình nếu cấu hình sai plot style. Luôn kiểm tra hoặc ép sang màu đen (TrueColor `0,0,0`) khi tạo layout xuất in ấn.

## 5. Cơ Chế Dự Phòng (Fallback)
- Nếu AutoCAD MCP Server không phản hồi hoặc lệnh vẽ bị treo:
  - Chuyển hướng xuất mã nguồn sang file script `.lsp` để người dùng nạp thủ công qua `APPLOAD`.
  - Hoặc tạo trực tiếp file `.dxf` bằng Python với thư viện `ezdxf` độc lập không cần mở AutoCAD.
