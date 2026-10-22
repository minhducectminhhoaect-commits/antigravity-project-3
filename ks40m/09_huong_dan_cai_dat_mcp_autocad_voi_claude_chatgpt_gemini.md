# Hướng dẫn cài đặt MCP AutoCAD với Claude, Chat GPT và Gemini?

- **URL:** https://lenote.dev/article/huong-dan-cai-dat-mcp-autocad-voi-claude-chat-gpt-va-gemini
- **Tác giả:** KS 4.0 Academy (@ks40m)
- **Ngày xuất bản:** 2026-05-03 (13:49:21 UTC)
- **Ngày cập nhật:** 2026-10-21 (02:10:47 UTC)
- **Chuyên mục:** Lập trình & AI
- **Từ khóa:** AutoCAD, AutoCAD MCP, Claude, Gemini, CHAT GPT
- **Thời lượng:** 9 phút đọc
- **Ảnh bìa:** https://lenotestore.blob.core.windows.net/uploads/images/1777795594971-maeico.webp

---

## Tóm tắt
Bạn muốn AI vẽ AutoCAD thay bạn? Bài này hướng dẫn từng bước cài MCP AutoCAD với Claude và Gemini CLI: từ Claude Desktop, Python, UV cho đến load LISP dispatcher. Tự động hóa workflow CAD trong vài phút.

---

## Nội dung bài viết

Trong bài này, mình sẽ hướng dẫn cài đặt MCP AutoCAD với Claude, ChatGPT và Gemini để bạn có thể kết nối AI trực tiếp với AutoCAD và tự động hóa quy trình vẽ.

# 1. Cài đặt Claude Desktop và tải AutoCAD MCP từ Github (link ở cuối bài viết)

## 1.1. Claude Desktop

**Claude Desktop** là ứng dụng **Claude** chạy trực tiếp trên máy tính. Khi dùng **Claude Desktop**, bạn có thể cấu hình thêm **MCP** để Claude kết nối với các công cụ bên ngoài như **AutoCAD**, file hệ thống, trình duyệt, database hoặc các ứng dụng nội bộ.

> Claude có bản **Free** (miễn phí, giới hạn usage), **Pro** (~20$/tháng), và **Max** (~100–200$/tháng cho người dùng nặng), ngoài ra còn có **Team** (~25$/user/tháng) và **Enterprise** (giá tùy chỉnh).

**Claude Desktop** hiện có bản cho **macOS** và **Windows** trên trang tải chính thức của Claude.

- **Bước 1**: Tải Claude Desktop: Truy cập trang tải chính thức của Claude: [https://claude.com/download](https://claude.com/download)
- **Bước 2**: Cài đặt ứng dụng: Mở file cài đặt **.exe**, sau đó làm theo hướng dẫn trên màn hình.
- **Bước 3**: Đăng nhập Claude: Mở Claude Desktop và đăng nhập bằng tài khoản Claude của bạn.

> Nếu **không nhận được OTP**, hãy dùng **số điện thoại ảo** (ưu tiên Nhật/Mỹ) hoặc thử nhà mạng khác Viettel như **MobiFone**, **VinaPhone**.

## 1.2. AutoCAD MCP Server

**AutoCAD MCP Server** là một **MCP server** viết bằng **Python** để làm trung gian giữa AI và AutoCAD, cho phép AI gửi lệnh (vẽ, sửa, đọc bản vẽ…) bằng text.

Nó là một "server điều khiển AutoCAD":

- **Nhận request** từ AI (Claude, ChatGPT…)
- **Thực thi** trong AutoCAD hoặc tạo DXF
- **Trả kết quả** lại cho AI

Hãy tải từ link Github trực tiếp, **giải nén** rồi lưu ở thư mục làm việc của bạn (xem trong video).

> **Lưu ý:** Chỉ hỗ trợ tốt cho **AutoCAD LT 2024+** trên **Windows** (vì cần **AutoLISP + Win32 IPC**), **không support AutoCAD LT Mac**.

---

# 2. Cài đặt Python và cài đặt môi trường cho MCP

## 2.1. Cài Python (Windows)

- Tải tại: [https://www.python.org/downloads/](https://www.python.org/downloads/)

> **Lưu ý:** Nhớ check vào: **Add Python to PATH** để bạn có thể gọi Python từ bất kỳ đâu trong CMD mà không cần chỉ định đường dẫn đầy đủ.

Kiểm tra:

```bash
python --version
pip --version
# Nếu hiện ra phiên bản Python như Python 3.x.x là cài thành công.
```

## 2.2. Cài UV (package manager) và các dependencies (thư viện phụ thuộc)

Nhấn **Win + R** → gõ `cmd` → Enter, hoặc mở **Command Prompt / PowerShell** từ Start, hoặc vào thư mục project rồi gõ `cmd` trên thanh địa chỉ để mở nhanh terminal tại đó.

```bash
pip install uv
```

Sau đó chạy:

```bash
uv sync
```

> Nếu không chạy được hãy thử **restart** CMD hoặc kiểm tra Python đã add PATH.

## 2.3. Cấu hình MCP cho Claude

- Tạo / mở file config Claude Desktop: File: `claude_desktop_config.json`
- Thêm cấu hình AutoCAD MCP như sau:

```json
{
  "mcpServers": {
    "autocad-mcp": {
      "command": "C:\\path\\to\\autocad-mcp\\.venv\\Scripts\\python.exe",
      "args": ["-m", "autocad_mcp"],
      "env": {
        "AUTOCAD_MCP_BACKEND": "auto"
      }
    }
  }
}
```

## 2.4. Kết nối và thử nghiệm trong AutoCAD LT

### 2.4.1. Đầu tiên load file LISP để AutoCAD nhận lệnh từ MCP Server (AI điều khiển)

Mở **AutoCAD LT (Windows 2024+)**, gõ `APPLOAD` → chọn file `mcp_dispatch.lsp` trong thư mục repo AutoCAD MCP.

> Bạn có thể add file LISP này vào **Startup Suite** (biểu tượng chiếc cặp trong APPLOAD) để mỗi lần mở CAD nó tự động nạp mà không cần thao tác lại.

### 2.4.2. Khởi động vòng lặp IPC trong AutoCAD

Gõ lệnh:

```
MCP_START
```

Nếu thành công, cửa sổ CAD sẽ báo dispatcher đã sẵn sàng lắng nghe request từ AI.

---

# 3. Cài đặt và cấu hình với Gemini CLI

## 3.1. Cài đặt Gemini CLI qua Node.js (npm)

Mở Terminal / PowerShell và chạy:

```bash
npm install -g @google/gemini-cli
```

Kiểm tra:

```bash
gemini --version
```

## 3.2. Cấu hình MCP cho Gemini CLI

Tạo hoặc mở file:

```
%USERPROFILE%\.gemini\settings.json
```

Thêm server:

```json
{
  "mcpServers": {
    "autocad-mcp": {
      "command": "C:\\path\\to\\autocad-mcp\\.venv\\Scripts\\python.exe",
      "args": ["-m", "autocad_mcp"]
    }
  }
}
```

## 3.3. Kiểm tra kết nối Gemini CLI

Mở Gemini CLI:

```bash
gemini
```

Sau đó chạy lệnh:

```
/mcp
```

Nếu thấy **`autocad-mcp`** xuất hiện trong danh sách server/tool thì **Gemini CLI đã nhận MCP thành công**.

---

# 4. Cài đặt Codex CLI để điều khiển AutoCAD

**Codex CLI** là **coding agent** của **OpenAI** chạy trực tiếp trong **Terminal**, mã nguồn mở và viết bằng **Rust** để tối ưu tốc độ. Codex CLI có sẵn trong các gói **ChatGPT Plus, Pro, Business, Edu, Enterprise** (hoặc dùng **API key**). Khi kết nối với **MCP Server**, Codex có thể **gửi lệnh tới AutoCAD**, **đọc dữ liệu bản vẽ** và hỗ trợ **tự động hóa thao tác CAD**.

> Codex CLI hỗ trợ cả **macOS, Windows, Linux**. Trên Windows có thể chạy native trong **PowerShell** hoặc dùng **WSL2** nếu cần môi trường Linux.

## 4.1. Cài Codex CLI

Mở **Terminal / PowerShell / CMD** và chạy:

```bash
npm install -g @openai/codex
```

Sau khi cài xong, kiểm tra:

```bash
codex --version
```

Chạy Codex CLI:

```bash
codex
```

Lần đầu mở, Codex CLI sẽ yêu cầu **đăng nhập ChatGPT** hoặc **dán API key**.

> Nếu muốn dùng API key thay vì đăng nhập ChatGPT, chạy: `codex login --api-key "your-key"`

## 4.2. Cấu hình MCP Server cho Codex CLI

Codex CLI dùng file **`config.toml`** (định dạng **TOML**, **khác với JSON** của Claude/Gemini) để cấu hình MCP Server.

Vị trí file cấu hình:

```
C:\Users\<ten-user>\.codex\config.toml
```

Nếu chưa có thư mục `.codex` hoặc file `config.toml`, hãy **tự tạo mới**.

Ví dụ cấu hình AutoCAD MCP Server:

```toml
[mcp_servers.autocad-mcp]
command = "C:\\path\\to\\autocad-mcp\\.venv\\Scripts\\python.exe"
args = ["-m", "autocad_mcp", "--stdio"]

[mcp_servers.autocad-mcp.env]
AUTOCAD_MCP_BACKEND = "auto"
```

Hoặc bạn có thể dùng lệnh **`codex mcp add`** để thêm MCP server bằng cách tương tác:

```bash
codex mcp add autocad-mcp --env AUTOCAD_MCP_BACKEND=auto -- C:\path\to\autocad-mcp\.venv\Scripts\python.exe -m autocad_mcp
```

Một số lệnh quản lý MCP hữu ích:

```bash
codex mcp list              # Liệt kê tất cả MCP server đã cấu hình
codex mcp get <name>        # Xem chi tiết một server
codex mcp remove <name>     # Xóa một server
```

## 4.3. Mở AutoCAD và load dispatcher

Trước khi dùng Codex điều khiển AutoCAD, hãy **mở AutoCAD trước** và **load file LISP** (xem mục **2.4.1**).
Nếu Codex gửi lệnh nhưng AutoCAD không phản hồi, hãy kiểm tra:

```
1. AutoCAD đã mở chưa
2. Dispatcher đã load trong AutoCAD chưa
3. Thư mục IPC có đúng không
4. Python MCP Server có chạy được không
5. Codex CLI đã nhận MCP Server chưa
```

## 4.4. Kiểm tra Codex CLI đã nhận MCP chưa

Cách 1 — chạy lệnh trong terminal:

```bash
codex mcp list
```

Nếu thấy **`autocad-mcp`** xuất hiện trong danh sách thì **Codex CLI đã nhận MCP thành công**.

Cách 2 — mở Codex CLI rồi kiểm tra trong session:

```bash
codex
```

Khi Codex chạy, nó sẽ **tự động khởi động các MCP server** đã cấu hình và **expose tools** của chúng cùng với các tool built-in.

> Cấu hình MCP trong `~/.codex/config.toml` được **chia sẻ giữa Codex CLI và Codex IDE Extension**, nên bạn chỉ cần setup **một lần**.

Nhờ Codex CLI, bạn có thêm một lựa chọn agent OpenAI bên cạnh Claude và Gemini để **gửi lệnh vẽ**, **đọc bản vẽ** và **tự động hóa workflow AutoCAD** ngay từ Terminal.

---

# 🔗 Link tải & tham khảo

- **Github AutoCAD MCP:** [https://github.com/ks40-academy/autocad-mcp](https://github.com/ks40-academy/autocad-mcp)
- **Claude Desktop:** [https://claude.com/download](https://claude.com/download)
- **Python (Windows):** [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **Gemini CLI (npm):** [https://geminicli.com](https://geminicli.com)
