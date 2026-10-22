# Gói Tích Hợp Toàn Diện AppSheet AI Agent cho Antigravity

Gói công cụ này cho phép **Antigravity AI Agent** đóng vai trò là bộ não điều hành toàn diện hệ thống **Google AppSheet**, bao gồm:
1. **Tạo App từ ý tưởng (Idea to App)**: Tự động thiết kế cấu trúc CSDL đa bảng (Key, Ref, Enum, Master-Detail) và sinh file Excel/Google Sheets chuẩn AppSheet.
2. **Đọc / Trích xuất dữ liệu**: Truy vấn dữ liệu có điều kiện lọc bằng Selector Expression.
3. **Đẩy / Đột biến dữ liệu**: Thêm (Add), Sửa (Edit), Xóa (Delete) bản ghi và kích hoạt Action.
4. **Hứng Trigger thời gian thực**: Lắng nghe Webhook khi người dùng thực hiện thao tác trên ứng dụng AppSheet.

---

## 📁 Cấu trúc thư mục

```
d:\antigravity 3\appsheet_mcp_server/
├── server.py              # MCP Server (Cung cấp tools cho Antigravity)
├── webhook_server.py       # FastAPI Webhook Hub hứng trigger từ AppSheet Bot
├── webhook_events.jsonl   # Log lưu trữ các sự kiện từ AppSheet
├── .env                   # Lưu App ID và Access Key
├── .env.example           # File mẫu biến môi trường
└── README.md              # Hướng dẫn chi tiết
```

---

## ⚙️ Cấu hình ban đầu

### 1. Lấy thông tin kết nối từ AppSheet
1. Mở ứng dụng trên [AppSheet](https://www.appsheet.com).
2. Vào **Manage** > **Integrations** > **In: from external services**.
3. Bật **Enable** mục API.
4. Nhấn **Create Application Access Key**.
5. Mở file `appsheet_mcp_server/.env` và điền:
   ```env
   APPSHEET_APP_ID=your_app_id_here
   APPSHEET_APPLICATION_ACCESS_KEY=your_access_key_here
   APPSHEET_WEBHOOK_PORT=8000
   ```

### 2. Cấu hình MCP Server trong Antigravity
Server đã được tự động đăng ký trong cấu hình toàn cục `~/.gemini/config/mcp_config.json`:
```json
{
  "mcpServers": {
    "appsheet": {
      "command": "python",
      "args": [
        "d:\\antigravity 3\\appsheet_mcp_server\\server.py"
      ],
      "env": {
        "PYTHONIOENCODING": "utf-8"
      }
    }
  }
}
```

---

## 🚀 Các kịch bản sử dụng

### Kịch bản 1: Yêu cầu Agent tạo App mới từ ý tưởng
Bạn chỉ cần nhắn vào khung chat Antigravity:
> *"Hãy tạo cho tôi một ứng dụng quản lý xuất nhập tồn kho có phê duyệt đơn hàng, gồm các bảng: Vật tư, Phiếu xuất nhập, Chi tiết phiếu, và Danh mục kho."*

Agent sẽ:
- Phân tích và sinh file Excel `.xlsx` với các bảng, liên kết `Ref`, khóa chính `Key`, trường `Enum` và dữ liệu mẫu.
- Xuất file tài liệu hướng dẫn từng bước kích hoạt app trên Google Drive chỉ với 1 click.

---

### Kịch bản 2: Yêu cầu Agent đọc & thao tác dữ liệu
Bạn nhắn:
> *"Lấy cho tôi danh sách các đơn hàng có trạng thái 'Chờ duyệt' trong AppSheet"*
> 
> *"Hãy thêm một sản phẩm mới vào bảng SanPham: Mã SP05, Tên Giày Sneaker Biti's Hunter, Giá 850000"*
> 
> *"Chuyển trạng thái của đơn hàng DH1002 sang 'Đã duyệt'"*

Agent sẽ tự động gọi các tool MCP tương ứng (`appsheet_find_records`, `appsheet_add_rows`, `appsheet_update_rows`).

---

### Kịch bản 3: Hứng Trigger thời gian thực từ AppSheet
Khi nhân viên bấm nút trên điện thoại qua AppSheet và bạn muốn Antigravity nhận được thông báo ngay lập tức:

#### Bước 1: Chạy Webhook Hub
Mở terminal và chạy:
```powershell
python "d:\antigravity 3\appsheet_mcp_server\webhook_server.py"
```

#### Bước 2: Tạo Public URL cho Webhook (để AppSheet từ internet gọi về được)
Dùng **Cloudflare Tunnel** (miễn phí, không cần tạo tài khoản):
```powershell
npx untun tunnel --port 8000
# Hoặc dùng ngrok / cloudflared:
# cloudflared tunnel --url http://localhost:8000
```
Bạn sẽ nhận được một đường link công khai, ví dụ: `https://something.trycloudflare.com`.

#### Bước 3: Cài đặt Bot trong AppSheet
1. Vào **Automation** > **Bots** > Tạo Bot mới.
2. **Event**: Chọn bảng và sự kiện (ví dụ: `Adds and Updates` trên bảng `DonHang`).
3. **Process Task**: Chọn **Call a Webhook**:
   - **Url**: `https://something.trycloudflare.com/webhook/appsheet`
   - **HTTP Verb**: `POST`
   - **HTTP Content Type**: `JSON`
   - **Body Template**:
     ```json
     {
       "event": "DonHang_Updated",
       "order_id": "<<[MaDon]>>",
       "status": "<<[TrangThai]>>",
       "user": "<<USEREMAIL()>>",
       "timestamp": "<<NOW()>>"
     }
     ```
4. Khi có người thao tác, dữ liệu sẽ tự động ghi vào `webhook_events.jsonl`, và Agent có thể đọc được ngay qua tool `appsheet_get_webhook_events`.
