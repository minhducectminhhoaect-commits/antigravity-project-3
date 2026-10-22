# Hướng dẫn tạo & Cấu hình App 'App_KiemDem_HangHoa' trên Google AppSheet

**Mô tả:** Ứng dụng quản lý thời gian bắt đầu/kết thúc và hoạt động kiểm đếm nhập/xuất hàng hóa đối chiếu giữa hồ sơ giấy tờ và thực tế kiểm đếm.

**File CSDL đi kèm:** [`App_KiemDem_HangHoa_Database.xlsx`](file:///d:/antigravity%203/App_KiemDem_HangHoa_Database.xlsx) (đã tạo sẵn tại thư mục hiện tại với 3 bảng và dữ liệu mẫu đầy đủ).

---

## 🚀 Bước 1: Khởi tạo App trên AppSheet (Chỉ mất 2 phút)

1. Tải file [`App_KiemDem_HangHoa_Database.xlsx`](file:///d:/antigravity%203/App_KiemDem_HangHoa_Database.xlsx) lên **Google Drive** của bạn (hoặc mở bằng Google Sheets).
2. Mở trình duyệt và truy cập: [**AppSheet Create from Data**](https://www.appsheet.com/Template/App/CreateFromData).
3. Chọn nguồn dữ liệu là file `App_KiemDem_HangHoa_Database` vừa tải lên.
4. Trong AppSheet Editor, vào tab **Data** > **Add Table** để thêm cả 3 bảng:
   - `PhieuKiemDem` (Bảng Cha - Quản lý phiên kiểm đếm, thời gian bắt đầu/kết thúc)
   - `ChiTietKiemDem` (Bảng Con - Kiểm từng mặt hàng, số lượng hồ sơ vs thực tế)
   - `DanhMucHangHoa` (Danh mục tra cứu chuẩn)

---

## 📐 Bước 2: Thiết lập Cột & Công thức tự động (AppSheet Formulas)

### 1. Bảng Con: `ChiTietKiemDem` (Master-Detail)
Vào **Data** > **Columns** > chọn bảng `ChiTietKiemDem`:
- **`MaPhieu`**: Kiểu `Ref` trỏ về bảng `PhieuKiemDem`. **Tích chọn `IsPartOf = TRUE`** *(Tính năng này giúp form con hiển thị lồng ngay trong form tạo phiếu cha)*.
- **`MaHang`**: Kiểu `Ref` trỏ về bảng `DanhMucHangHoa`.
- **`SoLuongHoSo`**: Kiểu `Decimal` (hoặc `Number`).
- **`SoLuongThucKiem`**: Kiểu `Decimal` (hoặc `Number`).
- **`ChenhLech`**:
  - Đặt công thức tại ô **App Formula**:
    ```excel
    [SoLuongThucKiem] - [SoLuongHoSo]
    ```
- **`KetLuanKiem`**:
  - Đặt công thức tại ô **App Formula**:
    ```excel
    IFS(
      ISBLANK([SoLuongThucKiem]), "Chưa kiểm",
      [SoLuongThucKiem] = [SoLuongHoSo], "Khớp",
      [SoLuongThucKiem] > [SoLuongHoSo], "Thừa hàng (+)",
      [SoLuongThucKiem] < [SoLuongHoSo], "Thiếu hàng (-)"
    )
    ```

---

### 2. Bảng Cha: `PhieuKiemDem`
Vào **Data** > **Columns** > chọn bảng `PhieuKiemDem`:
- **`MaPhieu`**: Kiểu `Text`, tích `Key`. Initial value: `UNIQUEID()`.
- **`GioBatDau`**: Kiểu `DateTime`. Initial value: `NOW()`.
- **`GioKetThuc`**: Kiểu `DateTime`.
- **`NguoiKiem`**: Kiểu `Text`. Initial value: `USEREMAIL()`.
- **Thêm Cột Ảo (Add Virtual Column) tính Thời Lượng Kiểm**:
  - Tên cột ảo: `ThoiLuongKiem`
  - App Formula:
    ```excel
    IF(
      ISNOTBLANK([GioKetThuc]),
      CONCATENATE(TOTALMINUTES([GioKetThuc] - [GioBatDau]), " phút"),
      "Đang tiến hành kiểm..."
    )
    ```
- **Thêm Cột Ảo Tổng Chênh Lệch**:
  - Tên cột ảo: `TongChenhLech`
  - App Formula:
    ```excel
    SUM([Related ChiTietKiemDems][ChenhLech])
    ```

---

## ⚡ Bước 3: Tạo 2 Nút bấm tự động (Actions) cho thời gian

Vào **Actions** (hoặc App logic) để tạo trải nghiệm bấm 1 chạm:

1. **Nút "Bắt đầu kiểm"**:
   - For a record of table: `PhieuKiemDem`
   - Do this: `Data: set the values of some columns in this row`
   - Set columns:
     - `GioBatDau` = `NOW()`
     - `TrangThai` = `"Đang kiểm"`
   - Appearance: Icon `Play`, màu Xanh dương.

2. **Nút "Hoàn tất kiểm đếm"**:
   - For a record of table: `PhieuKiemDem`
   - Do this: `Data: set the values of some columns in this row`
   - Set columns:
     - `GioKetThuc` = `NOW()`
     - `TrangThai` = `IF(SUM([Related ChiTietKiemDems][ChenhLech]) = 0, "Khớp hồ sơ", "Có chênh lệch")`
   - Appearance: Icon `Check`, màu Xanh lá.

---

## 🎨 Bước 4: Định dạng màu sắc cảnh báo (Format Rules)

Vào **UX** > **Format Rules** > Thêm 3 rule trực quan:

1. **Hàng thiếu (Cảnh báo Đỏ ⚠️)**:
   - Table: `ChiTietKiemDem`
   - Condition: `[ChenhLech] < 0`
   - Format: Màu chữ Đỏ, Icon `Alert-triangle`, bôi đậm.
2. **Hàng thừa (Cảnh báo Vàng/Cam ⚠️)**:
   - Table: `ChiTietKiemDem`
   - Condition: `[ChenhLech] > 0`
   - Format: Màu chữ Cam, Icon `Alert-circle`.
3. **Khớp số lượng (Xanh lá ✅)**:
   - Table: `ChiTietKiemDem`
   - Condition: `AND(ISNOTBLANK([SoLuongThucKiem]), [ChenhLech] = 0)`
   - Format: Màu chữ Xanh lá, Icon `Check-circle`.

---

## 🤖 Bước 5: Kết nối Antigravity điều khiển App này

Sau khi tạo xong app trên AppSheet, bạn lấy **App ID** và **Access Key** dán vào file [`.env`](file:///d:/antigravity%203/appsheet_mcp_server/.env).

Lúc này, bạn có thể ra lệnh cho Antigravity ngay trong chat:
- *"Kiểm tra xem hôm nay có phiếu kiểm đếm nào có chênh lệch không?"*  
  -> Antigravity gọi `appsheet_find_records(table_name='PhieuKiemDem', selector='[TrangThai] = "Có chênh lệch"')`.
- *"Tự động thêm phiếu kiểm mới từ tờ khai hải quan số TK9921 cho lô hàng nhập lúc 14:00"*  
  -> Antigravity tự động đẩy phiếu cha và danh sách chi tiết hàng hóa vào AppSheet qua `appsheet_add_rows`.
