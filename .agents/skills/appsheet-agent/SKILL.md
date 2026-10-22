---
name: appsheet-agent
description: >-
  Điều khiển, tương tác và tự động hóa toàn diện với Google AppSheet như một AI Agent chuyên nghiệp.
  Kích hoạt khi người dùng yêu cầu: tạo ứng dụng AppSheet từ ý tưởng nghiệp vụ, thiết kế cấu trúc database
  chuẩn (Key, Ref, Enum, Master-Detail), đọc/trích xuất dữ liệu từ AppSheet, tự động đẩy/sửa/xóa dữ liệu,
  kích hoạt Custom Action, hoặc cấu hình và lắng nghe Webhook/Trigger từ AppSheet Automation Bot.
---

# AppSheet AI Agent Skill

Kỹ năng này trao cho Antigravity năng lực điều hành và tương tác 2 chiều với hệ sinh thái **Google AppSheet**:

```
[Người dùng nêu ý tưởng / Thao tác trên App]
                     │
                     ▼
             [ANTIGRAVITY AGENT]
         ┌───────────┼───────────┐
         ▼           ▼           ▼
   [Tạo CSDL]   [Gọi API]   [Hứng Trigger]
   (Excel/Drive) (Find/Add) (Webhook Hub)
         │           │           ▲
         └───────────┼───────────┘
                     ▼
             [GOOGLE APPSHEET]
```

---

## 1. Các công cụ MCP có sẵn (`appsheet`)

Agent sử dụng các công cụ sau được cung cấp qua MCP Server `appsheet`:

1. **`appsheet_scaffold_app`**:
   - Biến mô tả nghiệp vụ thành file Excel đa bảng (.xlsx) định dạng tối ưu cho AppSheet.
   - Thiết lập đúng: Cột Khóa chính (`Key`), Cột Nhãn (`Label`), Khóa ngoại (`Ref`), Trạng thái (`Enum`), và sinh hàng dữ liệu mẫu.
   - Tự động sinh file `Setup_Guide.md` hướng dẫn tải lên Google Drive và khởi tạo AppSheet với 1 click.

2. **`appsheet_find_records`**:
   - Truy vấn bản ghi từ bảng bất kỳ trên AppSheet.
   - Hỗ trợ biểu thức Selector: ví dụ `[TrangThai] = 'Chờ duyệt'` hoặc `Filter(DonHang, [TongTien] > 1000000)`.

3. **`appsheet_add_rows`**:
   - Đẩy hàng dữ liệu mới vào bảng (tự động điền dữ liệu, tạo đơn, tạo báo cáo).

4. **`appsheet_update_rows`**:
   - Cập nhật thông tin dòng (ví dụ: chuyển trạng thái sang "Đã duyệt", cập nhật số lượng tồn kho).

5. **`appsheet_delete_rows`**:
   - Xóa dòng theo Key ID.

6. **`appsheet_invoke_action`**:
   - Kích hoạt Action tùy biến đã cấu hình trên AppSheet (ví dụ: gửi thông báo, in PDF, kích hoạt quy trình).

7. **`appsheet_get_webhook_events`**:
   - Đọc các sự kiện mới nhất mà AppSheet Automation Bot vừa gửi về máy chủ trung gian.

8. **`appsheet_get_architecture_guide`**:
   - Tra cứu quy tắc thiết kế công thức, bảo mật và logic AppSheet.

---

## 2. Quy trình làm việc chuẩn của Agent

### Quy trình 1: Tạo App từ ý tưởng người dùng
1. **Lắng nghe & Phân tích nghiệp vụ**:
   - Xác định các đối tượng chính (Entities).
   - Xác định quan hệ: 1-1, 1-N (Master-Detail, ví dụ: Đơn hàng ⟷ Chi tiết đơn hàng).
   - Xác định quy trình trạng thái (Workflow stages).
2. **Thiết kế Schema chuẩn AppSheet**:
   - Luôn tạo cột khóa chính `ID` (Initial value: `UNIQUEID()`).
   - Cột liên kết luôn đặt tên theo bảng tham chiếu và kiểu `Ref`.
   - Các cột trạng thái dùng `Enum`.
3. **Gọi `appsheet_scaffold_app`**:
   - Sinh file `.xlsx` và tài liệu hướng dẫn.
   - Cung cấp link mở nhanh [AppSheet Create from Data](https://www.appsheet.com/Template/App/CreateFromData).

---

### Quy trình 2: Tương tác Dữ liệu 2 chiều (Đọc / Ghi)
1. Kiểm tra cấu hình `APPSHEET_APP_ID` và `APPSHEET_APPLICATION_ACCESS_KEY` trong file `appsheet_mcp_server/.env`.
2. Khi người dùng yêu cầu kiểm tra/báo cáo: Gọi `appsheet_find_records`.
3. Khi người dùng yêu cầu cập nhật hoặc tự động ghi nhận dữ liệu: Gọi `appsheet_add_rows` hoặc `appsheet_update_rows`.

---

### Quy trình 3: Nhận Trigger từ AppSheet khi có người thao tác
1. Khởi động Webhook Listener cục bộ:
   ```powershell
   python "d:\antigravity 3\appsheet_mcp_server\webhook_server.py"
   ```
2. Trong AppSheet Console:
   - Vào **Automation** > **Bots** > Thêm Bot mới:
     - **Event**: Data Change (Adds, Updates, hoặc Deletes).
     - **Run a task**: Chọn *Call a Webhook*.
     - **URL**: Điền địa chỉ webhook (dùng ngrok/Cloudflare tunnel nếu trên internet, ví dụ `https://your-domain.trycloudflare.com/webhook/appsheet`).
     - **HTTP Method**: POST.
     - **HTTP Body Type**: JSON.
3. Khi sự kiện xảy ra, Agent gọi `appsheet_get_webhook_events` để lấy thông tin người dùng vừa thao tác và thực hiện chuỗi hành động thông minh tiếp theo.
