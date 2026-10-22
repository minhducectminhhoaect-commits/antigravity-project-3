# Hướng dẫn thiết lập App 'Quản Lý Sự Cố, Bảo Trì & Đèn Andon Nhà Xưởng' (CMMS)

**Mô tả:** Hệ thống số hóa toàn diện quy trình xử lý sự cố thiết bị máy móc theo 5 vai trò thực tế nhà xưởng (Tổ trưởng chuyền, Thợ bảo trì, TechLead, Thủ kho phụ tùng, và Ban Giám đốc).

**File CSDL hoàn chỉnh:** [`App_BaoTri_Andon_NhaXuong_Database.xlsx`](file:///d:/antigravity%203/App_BaoTri_Andon_NhaXuong_Database.xlsx) *(đã khởi tạo sẵn với 6 bảng chuẩn và dữ liệu thực tế)*.

---

## 🏛️ Sơ đồ 5 Tầng Phân Quyền & Luồng Dữ Liệu

```
[1. TỔ TRƯỞNG CHUYỀN] ──(Quét QR Báo hư)──► [YeuCauSuaChua: Đèn ĐỎ 🔴]
                                                        │
[2. THỢ BẢO TRÌ] ◄──(Nghe đọc / Nhận việc)──────────────┘
       │
       ├──(Điểm danh tại máy)──► [Đèn VÀNG 🟡 - Bắt đầu đo giờ sửa]
       │
       └──(Sửa quá 15 phút?)──► [3. TECHLEAD Quyết định Đổi máy tạm 🟣]
       │
       └──(Xin linh kiện)─────► [4. THỦ KHO: Gán mã 8 số -> Xuất kho]
       │
       ▼
[Khai bệnh án máy móc & Báo sửa xong] ──► [Đèn LAM 🔵]
                                                │
[1. TỔ TRƯỞNG CHẠY THỬ NGHIỆM THU] ────────────┘
       │
       ▼ (Đạt chuẩn chất lượng)
[ĐÓNG PHIẾU - ĐÈN XANH 🟢] ──► [5. DASHBOARD GIÁM ĐỐC / TV ANDON]
```

---

## 📐 Cấu hình Cột & Công thức thông minh trên AppSheet

### 1. Bảng `YeuCauSuaChua` (Bảng Master)
* **`MaMay`**: Kiểu `Ref` trỏ về `DanhMucThietBi`. **Bật tính năng `Scannable = TRUE`** để mở camera quét mã QR/Barcode trên thân máy.
* **`MaChuyen`**: Kiểu `Ref` trỏ về `DanhMucChuyen`.
* **`ThoChinh`**: Kiểu `Ref` trỏ về `NhanSuKyThuat`.
* **Cột ảo tính Thời gian Phản ứng (Phút):**
  - Tên: `ThoiGianPhanUng`
  - Formula:
    ```excel
    IF(ISNOTBLANK([ThoiGianThoDen]), TOTALMINUTES([ThoiGianThoDen] - [ThoiGianBaoHu]), TOTALMINUTES(NOW() - [ThoiGianBaoHu]))
    ```
* **Cột ảo tính Thời gian Thợ sửa chữa (Phút):**
  - Tên: `ThoiGianSuaChua`
  - Formula:
    ```excel
    IF(ISNOTBLANK([ThoiGianSuaXong]), TOTALMINUTES([ThoiGianSuaXong] - [ThoiGianThoDen]), TOTALMINUTES(NOW() - [ThoiGianThoDen]))
    ```
* **Cột ảo Cảnh báo Sửa quá 15 phút (Cứu chuyền):**
  - Tên: `CanhBaoSuaQua15Phut`
  - Formula:
    ```excel
    AND(
      [TrangThaiSuaChua] = "2. Đang sửa (Vàng)",
      TOTALMINUTES(NOW() - [ThoiGianThoDen]) >= 15,
      [CoDoiMayTam] = "Không"
    )
    ```
* **Cột ảo Tính Tổng Thời gian Dừng chuyền (Downtime):**
  - Tên: `TongDowntimePhut`
  - Formula:
    ```excel
    IF(
      [CoDoiMayTam] = "Đã đổi máy tạm",
      TOTALMINUTES([ThoiGianDoiMay] - [ThoiGianBaoHu]),
      IF(ISNOTBLANK([ThoiGianNghiemThu]), TOTALMINUTES([ThoiGianNghiemThu] - [ThoiGianBaoHu]), TOTALMINUTES(NOW() - [ThoiGianBaoHu]))
    )
    ```

---

### 2. Bảng `YeuCauPhuTung` (Chi tiết linh kiện - `IsPartOf = TRUE`)
* **`MaPhieu`**: Kiểu `Ref` trỏ về `YeuCauSuaChua`. Bật `IsPartOf = TRUE`.
* **`MaPhuTung8So`**: Kiểu `Ref` trỏ về `DanhMucPhuTung`.
* **`ThanhTien`**:
  ```excel
  [SoLuongXin] * [DonGia]
  ```

---

## ⚡ Thiết lập 4 Nút Bấm 1 Chạm (Actions)

1. **Nút "Thợ đã có mặt tại máy" (Dành cho Thợ):**
   - Bảng: `YeuCauSuaChua`
   - Set column values:
     - `ThoiGianThoDen` = `NOW()`
     - `TrangThaiSuaChua` = `"2. Đang sửa (Vàng)"`
     - `ThoChinh` = `LOOKUP(USEREMAIL(), "NhanSuKyThuat", "Email", "MaTho")`
   - Only if condition: `[TrangThaiSuaChua] = "1. Chờ thợ (Đỏ)"`

2. **Nút "Quyết định Đổi máy tạm" (Dành cho TechLead):**
   - Chuyển sang form nhập `MaMayTam`, tự động gán `ThoiGianDoiMay = NOW()` và `TrangThaiSuaChua = "4. Đổi máy tạm (Tím)"`.

3. **Nút "Báo sửa xong" (Dành cho Thợ):**
   - Set column values:
     - `ThoiGianSuaXong` = `NOW()`
     - `TrangThaiSuaChua` = `"5. Chờ nghiệm thu"`
   - Chỉ hiện khi thợ đã điền `NguyenNhanHuHong` và `BienPhapXuLy`.

4. **Nút "Nghiệm thu đạt chuẩn - Đóng phiếu" (Dành cho Tổ trưởng):**
   - Set column values:
     - `ThoiGianNghiemThu` = `NOW()`
     - `NguoiNghiemThu` = `USEREMAIL()`
     - `DanhGiaChatLuong` = `"Đạt chuẩn sản xuất"`
     - `TrangThaiSuaChua` = `"6. Hoàn tất (Xanh)"`

---

## 🖥️ Màn hình TV Andon Xưởng (Dashboard View)

Tạo một Dashboard View trên AppSheet đặt tên là **"Andon Board"**:
- **Khối 1: Đèn Đỏ chớp nháy (Chờ thợ)**: Lọc các phiếu `[TrangThaiSuaChua] = "1. Chờ thợ (Đỏ)"`.
- **Khối 2: Cảnh báo Tím (Sửa quá 15 phút cần đổi máy)**: Lọc các phiếu `[CanhBaoSuaQua15Phut] = TRUE`.
- **Khối 3: Đang sửa chữa (Đèn Vàng)**.
- **Khối 4: Biểu đồ KPI (MTTR - Thời gian sửa trung bình & Top 5 máy hay hỏng nhất)**.
