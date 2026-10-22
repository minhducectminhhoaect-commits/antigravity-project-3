# Phần 1: Hướng dẫn cài đặt Revit MCP với Claude

- **URL:** https://lenote.dev/article/phan-1-huong-dan-cai-dat-revit-mcp-voi-claude
- **Tác giả:** KS 4.0 Academy (@ks40m)
- **Ngày xuất bản:** 2026-06-01 (13:21:14 UTC)
- **Ngày cập nhật:** 2026-10-20 (23:33:08 UTC)
- **Chuyên mục:** Lập trình & AI
- **Từ khóa:** AI, Revit, REVIT MCP, Claude, Gemini, CODEX, Antigravity
- **Ảnh bìa:** https://lenotestore.blob.core.windows.net/uploads/images/1780293695103-zkbjvu.webp

---

## Tóm tắt
Trong phần này, mình sẽ hướng dẫn cài đặt Revit MCP chi tiết từ bước chuẩn bị môi trường, cài đặt plugin, cấu hình MCP Server đến kết nối với các công cụ AI, giúp bạn nhanh chóng triển khai và sử dụng hiệu quả.

---

## Nội dung bài viết

# 1. Cài Đặt Revit MCP Plugin

Revit MCP Plugin hỗ trợ Autodesk Revit từ phiên bản 2020 đến 2026. Việc cài đặt được thực hiện thông qua Revit MCP Installer và chỉ mất vài phút để hoàn thành.

## Yêu Cầu Hệ Thống

Revit MCP Installer hỗ trợ hệ điều hành Windows 10 và Windows 11 phiên bản 64-bit. Để sử dụng Plugin, máy tính cần cài đặt Autodesk Revit từ phiên bản 2020 đến 2026. Ngoài ra, ứng dụng yêu cầu .NET 8 Desktop Runtime để hoạt động. Nếu máy tính chưa được cài đặt .NET 8 Desktop Runtime, Windows sẽ tự động hiển thị thông báo và hướng dẫn tải về từ Microsoft khi khởi chạy ứng dụng.

## Bước 1: Tải Về Và Giải Nén

Tải bộ cài đặt Revit MCP Plugin Installer ở link cuối bài viết.
Sau khi tải xong, giải nén file ZIP vào một thư mục bất kỳ trên máy tính.

## Bước 2: Khởi Chạy Revit MCP Installer

Mở file:

```
Revit MCP Installer.exe
```

Sau khi khởi động, ứng dụng sẽ hiển thị danh sách các phiên bản Revit được hỗ trợ cùng trạng thái cài đặt hiện tại.

## Bước 3: Chọn Phiên Bản Revit

Sử dụng công tắc bật/tắt để lựa chọn các phiên bản Revit muốn cài đặt Plugin.

![Chọn phiên bản cài đặt](https://lenotestore.blob.core.windows.net/uploads/images/1780294703557-jcudxo.webp)

## Bước 4: Cài Đặt Plugin

Nhấn nút **Install** để bắt đầu quá trình cài đặt cho các phiên bản Revit đã chọn.

![Cài đặt thành công](https://lenotestore.blob.core.windows.net/uploads/images/1780294740300-ud394h.webp)

## Bước 5: Khởi Động Revit

Sau khi cài đặt hoàn tất:

1. Đóng Revit nếu đang mở.
2. Khởi động lại Revit.
3. Mở bất kỳ Project nào.
4. Kiểm tra tab **Add-Ins** trên thanh Ribbon.

Nếu Revit MCP xuất hiện trong danh sách Add-Ins, việc cài đặt đã thành công.

![Screenshot 2026-06-01 152113.png](https://lenotestore.blob.core.windows.net/uploads/images/1780295054964-dckkem.webp)

## Gỡ Cài Đặt Plugin

Để gỡ bỏ Revit MCP khỏi máy tính:

1. Mở **Revit MCP Installer**.
2. Chọn các phiên bản Revit cần gỡ.
3. Nhấn nút **Uninstall**.

---

# 2. Cài Đặt Revit MCP Server

Sau khi cài đặt Revit MCP Plugin trong Autodesk Revit, bước tiếp theo là cài đặt Revit MCP Server. Thành phần này đóng vai trò cầu nối giữa Revit và các ứng dụng AI hỗ trợ giao thức MCP như Claude Desktop, Claude Code, Codex, Cline hoặc các MCP Client khác.

## Bước 1: Tải Về Và Giải Nén

Tải mã nguồn Revit MCP và giải nén vào một thư mục bất kỳ trên máy tính.

Ví dụ:

```
revit-mcp/
├── src/
├── build/
├── package.json
└── setup.bat
```

## Bước 2: Cài Đặt Node.js

Revit MCP Server yêu cầu Node.js phiên bản 18 trở lên để hoạt động.

Nếu máy tính chưa cài đặt Node.js:

1. Truy cập trang chính thức: [https://nodejs.org](https://nodejs.org/)
2. Tải phiên bản **LTS (Recommended For Most Users)**.
3. Chạy bộ cài đặt và hoàn tất quá trình cài đặt.
4. Mở Command Prompt hoặc Terminal và kiểm tra bằng lệnh:

```bash
node -v
```

Nếu xuất hiện số phiên bản, ví dụ:

```
v22.17.0
```

thì Node.js đã được cài đặt thành công.

## Bước 3: Cài Đặt Và Build Revit MCP

### Cách 1: Cài Đặt Tự Động (Khuyến Nghị)

Mở thư mục dự án và chạy file:

```
setup.bat
```

Script sẽ tự động cài đặt các thư viện cần thiết và build dự án.

### Cách 2: Cài Đặt Thủ Công

Mở Command Prompt hoặc Terminal tại thư mục dự án và chạy:

```bash
npm install
npm run build
```

Sau khi hoàn thành, thư mục `build` sẽ được tạo và Revit MCP Server đã sẵn sàng sử dụng.

Sau khi hoàn tất các bước trên, Revit MCP Server đã được cài đặt thành công. Bạn có thể tiếp tục sang bước cấu hình MCP Client để kết nối các ứng dụng AI với Autodesk Revit.

---

# 3. Cấu Hình Ứng Dụng AI

Sau khi cài đặt Revit MCP Server, bạn cần cấu hình ứng dụng AI để kết nối với Revit MCP. Sau khi cấu hình thành công, AI sẽ có thể truy cập các công cụ do Revit MCP cung cấp và tương tác trực tiếp với Autodesk Revit.

## Cài cho Claude Desktop

### Bước 1: Mở Cài Đặt MCP

Mở **Claude Desktop**.

Tại giao diện chính:

1. Nhấn vào ảnh đại diện ở góc dưới bên trái.
2. Chọn **Settings**.
3. Chọn **Extensions**.
4. Nhấn **Advanced Settings**.
5. Chọn **Edit Config**.

Claude Desktop sẽ tự động mở file cấu hình:

`%APPDATA%\Claude\claude_desktop_config.json`

Thông thường file này nằm tại:

`C:\Users\<User>\AppData\Roaming\Claude\claude_desktop_config.json`

### Bước 2: Thêm Revit MCP

Thêm cấu hình sau vào file claude_desktop_config.json:

```json
{
    "mcpServers": {
        "revit-mcp": {
            "command": "node",
            "args": [
                "C:\\Users\\rin\\Desktop\\Workspace\\revit-mcp\\revit-mcp-main\\build\\index.js"
            ]
        }
    }
}
```

Lưu file cấu hình sau khi chỉnh sửa.

### Bước 3: Khởi Động Lại Claude Desktop

Đóng hoàn toàn Claude Desktop và mở lại ứng dụng.

---

# Kết nối Claude với REVIT

1. Cài đặt cấp phép lệnh cho MCP: Mở Revit → Add-Ins → Click vào Settings thì cửa sổ cài đặt tập lệnh hiện ra. Chọn tất cả các lệnh như hình dưới và lưu lại.

![Screenshot 2026-06-01 at 18.43.16.png](https://lenotestore.blob.core.windows.net/uploads/images/1780307154596-fxrv24.webp)

2. Mở kết nối: Click vào Revit MCP Switch để mở kết nối.

---

# Link tải tài liệu

1. [Trình cài đặt Revit MCP Plugin](https://drive.google.com/file/d/1ItAVzd3_E2HU1iiootid9oin4aKTUsni/view?usp=sharing)
2. [Revit MCP Server](https://drive.google.com/file/d/1F_qTiKQHh3A68zqwTRyhYvl1cOCEPxRd/view?usp=sharing)
