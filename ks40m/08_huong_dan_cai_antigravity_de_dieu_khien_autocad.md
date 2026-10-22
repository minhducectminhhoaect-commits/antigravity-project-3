# Hướng dẫn cài Antigravity để điều khiển AutoCAD

- **URL:** https://lenote.dev/article/huong-dan-cai-antigravity-de-dieu-khien-autocad
- **Tác giả:** KS 4.0 Academy (@ks40m)
- **Ngày xuất bản:** 2026-05-10 (09:30:51 UTC)
- **Ngày cập nhật:** 2026-10-21 (02:01:00 UTC)
- **Chuyên mục:** Lập trình & AI
- **Từ khóa:** AutoCAD, AutoCAD MCP, Antigravity
- **Thời lượng:** 4 phút đọc
- **Ảnh bìa:** https://lenotestore.blob.core.windows.net/uploads/images/1778404435851-c8uyrv.webp

---

## Tóm tắt
Hướng dẫn từng bước cho kỹ sư BIM/AutoCAD trên Windows. Dành cho người đã có sẵn AutoCAD MCP server (Python) và muốn chuyển sang Antigravity IDE.

---

## Nội dung bài viết

# Hướng dẫn cài Google Antigravity & config AutoCAD MCP Server

> Hướng dẫn từng bước cho kỹ sư BIM/AutoCAD trên Windows. Dành cho người đã có sẵn AutoCAD MCP server (Python) và muốn chuyển sang Antigravity IDE. Nếu không thì xem bài trước.

# 1. Google Antigravity là gì?

**Google Antigravity** là agentic IDE mới của Google, ra mắt 11/2025 cùng Gemini 3. Khác với Cursor hay VS Code Copilot, Antigravity được thiết kế cho **autonomous agent workflow** — agent có thể plan, code, test và verify cả task lớn mà không cần can thiệp từng bước.

**Tại sao dùng Antigravity cho BIM workflow?**

- Hỗ trợ **multi-model** (Gemini 3 Pro, Claude Sonnet 4.5, GPT-OSS) — switch tùy task.
- **Agent Manager dashboard** chạy nhiều agents song song (vẽ grid + tạo dimension + xuất Excel cùng lúc).
- **Browser-in-the-loop** — agent test web app trực tiếp.
- **MCP support** chuẩn JSON config — tương thích AutoCAD/Revit MCP server có sẵn.

---

# 2. Cài đặt Google Antigravity

### Bước 2.1 — Tải installer

Vào [https://antigravity.google/download](https://antigravity.google/download) và chọn version phù hợp:

- **Windows**: `Antigravity-Setup-x64.exe` (~150-200 MB)

### Bước 2.2 — Cài đặt

#### Windows

1. Double-click file `.exe`.
2. Làm theo wizard, accept license.
3. Chọn install location (default: `C:\Users\<USER>\AppData\Local\Programs\Antigravity`).
4. Tick "Add to PATH" và "Create desktop shortcut".

### Bước 2.3 — Đăng nhập & setup ban đầu

1. Mở Antigravity → **Sign in with Google**.
2. Chọn AI model mặc định (có thể đổi sau):
   - **Gemini 3 Pro** — model native, free tier rộng nhất.
   - **Claude Sonnet 4.5** — tốt cho code-heavy task.
   - **GPT-OSS** — open-source fallback.
3. Chọn **autonomy preset**:
   - `Review-driven development` (khuyến nghị cho người mới) — agent dừng để review từng step.
   - `Autonomous` — agent chạy hết task rồi báo kết quả.

> **Quota lưu ý**: Free tier khoảng 20 requests/ngày với Gemini 3 Flash. Pro tier $20/tháng nếu dùng nhiều.

---

## 3. Config MCP server trong Antigravity

### Bước 3.1 — Mở `mcp_config.json`

Trong Antigravity:

1. Mở project bất kỳ (File → Open Folder).
2. Tìm **Agent pane** ở cột bên phải.
3. Click icon `⋯` (more_horiz) ở phía trên Agent pane.
4. Chọn **MCP Servers** → **Manage MCP Servers**.
5. Click **View raw config** ở góc trên panel.

File `mcp_config.json` sẽ mở. Path mặc định:

```
C:\Users\<USER>\.gemini\antigravity\mcp_config.json
```

### Bước 3.2 — Paste config

Thay thế nội dung file bằng:

```json
{
    "security": {
        "auth": {
            "selectedType": "oauth-personal"
        }
    },
    "mcpServers": {
        "autocad-mcp": {
            "command": "C:\\Dev\\autocad-mcp\\.venv\\Scripts\\python.exe",
            "args": [
                "-m",
                "autocad_mcp"
            ],
            "env": {
                "AUTOCAD_MCP_BACKEND": "auto"
            }
        }
    }
}
```

> **Lưu ý JSON syntax**:
> - Backslash phải escape: `\\` (không phải `\`).
> - Hoặc dùng forward slash: `C:/Dev/autocad-mcp/.venv/Scripts/python.exe` cũng hợp lệ.
> - Không được có comment `//` trong JSON — sẽ parse lỗi.

### Bước 3.3 — Save & Refresh

1. `Ctrl+S` để save file.
2. Quay lại **Manage MCP Servers** panel.
3. Click **Refresh** ở góc trên.
4. Đợi 2-5 giây để Antigravity spawn MCP process.

---

## 4. Verify & Test

### Bước 4.1 — Check status

Trong panel **Manage MCP Servers**, dưới mục **INSTALLED MCP SERVERS**, bạn sẽ thấy:

| Status | Ý nghĩa |
| --- | --- |
| 🟢 Active | Server start OK, hiện số tools (kỳ vọng: 30) |
| 🟡 Loading | Đang khởi động, đợi vài giây |
| 🔴 Error | Click vào để xem stderr log |

### Bước 4.2 — List tools

Click vào `autocad-mcp` để expand, xem danh sách 30 tools. Verify một số tool quan trọng:

- `make_grid` — vẽ grid system
- `add_griddim` — dimension cho grid
- `create_foundation_plan` — vẽ móng
- `export_quantity_excel` — xuất bảng thống kê

### Bước 4.3 — Test với agent

1. **Mở AutoCAD LT 2024 trước** — đảm bảo `mcp_dispatch.lsp` đã loaded.
2. Trong Antigravity, mở Agent panel, switch model sang **Claude Sonnet 4.5** (chạy MCP tool tốt hơn Gemini).
3. Test prompt:

```
Dùng autocad-mcp:
1. Vẽ grid 5x5, khoảng cách trục X = 6000mm, trục Y = 4500mm
2. Đặt tên trục: A,B,C,D,E (X) và 1,2,3,4,5 (Y)
3. Thêm dimension cho toàn bộ grid
4. Sau đó list ra coordinates của tất cả intersection points
```

Agent sẽ:
- Plan 4 bước trong **Markdown artifact** bên phải.
- Gọi tool `make_grid`, `add_griddim` lần lượt.
- Verify từng step bằng cách query lại AutoCAD.
- Tổng kết kết quả ở cuối.

---

# Tài liệu tham khảo

- Antigravity Docs: [https://antigravity.google/docs](https://antigravity.google/docs)
- MCP Specification: [https://modelcontextprotocol.io](https://modelcontextprotocol.io)
- AutoCAD .NET API: [https://help.autodesk.com/view/OARX/2024/ENU](https://help.autodesk.com/view/OARX/2024/ENU)
