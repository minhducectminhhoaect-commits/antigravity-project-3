# Revit Plugin Skill For C#

- **URL:** https://lenote.dev/article/revit-plugin-skill-for-c
- **Tác giả:** KS 4.0 Academy (@ks40m)
- **Ngày xuất bản:** 2026-07-17 (17:01:48 UTC)
- **Ngày cập nhật:** 2026-10-20 (16:42:28 UTC)
- **Chuyên mục:** Lập trình & AI
- **Từ khóa:** AGENT SKILL, CHAT GPT, Gemini, Claude
- **Ảnh bìa:** https://lenotestore.blob.core.windows.net/uploads/images/1784195719617-o8kq7t.webp

---

## Tóm tắt
Revit C# Skill có thể hiểu là một “bộ hướng dẫn” giúp AI biết cách tạo công cụ tự động cho Revit. Thay vì kỹ sư phải lặp lại nhiều thao tác thủ công, AI có thể hỗ trợ tạo plugin để tự động vẽ, kiểm tra mô hình, cập nhật dữ liệu hoặc xuất báo cáo.

---

## Nội dung bài viết

Revit C# Skill là một bộ hướng dẫn giúp AI hiểu cách phát triển plugin cho Revit: từ tạo tường, sàn, cột, Family, chỉnh sửa Parameter đến xây dựng giao diện và tự động hóa quy trình BIM.

### Lợi ích

Sau khi cài Skill, Gemini, Claude Code hoặc Codex sẽ:

- Viết code Revit API đúng cấu trúc hơn.
- Biết khi nào cần sử dụng Transaction và ExternalEvent.
- Tự chuyển đổi đơn vị giữa mm và đơn vị nội bộ của Revit.
- Hỗ trợ Revit 2022–2026.
- Giảm lỗi do AI tự đoán sai cách hoạt động của Revit.
- Có thể kết hợp với Revit MCP để kiểm tra mô hình, chạy thử code và xác minh kết quả.

Nói đơn giản, thay vì chỉ là một AI biết viết C#, AI sẽ có thêm “kiến thức nghề” của một lập trình viên Revit.

### Cách cài đặt

Trước tiên, tải file Skill về và giải nén. Sau đó, copy **revit-csharp-addin** trong folder của các AI tương ứng:

```
agent-skill/
├── claude/
│   └── revit-csharp-addin/
│       ├── SKILL.md
│       ├── references/
│       └── assets/
│
├── codex/
│   └── revit-csharp-addin/
│       ├── SKILL.md
│       ├── references/
│       └── assets/
│
└── gemini/
    └── revit-csharp-addin/
        ├── SKILL.md
        ├── references/
        └── assets/
```

Sau khi tải và giải nén, hãy copy thư mục tương ứng:

```
agent-skill\claude\revit-csharp-addin
→ .claude\skills\revit-csharp-addin
```

```
agent-skill\codex\revit-csharp-addin
→ .agents\skills\revit-csharp-addin
```

```
agent-skill\gemini\revit-csharp-addin
→ .agents\skills\revit-csharp-addin
```

Mỗi thư mục `revit-csharp-addin` phải chứa trực tiếp file `SKILL.md`, cùng với hai thư mục `references` và `assets`.

### Cài cho Codex

Cài riêng trong project:
```
<project>\.agents\skills\revit-csharp-addin\
```

Hoặc cài global để dùng cho mọi project:
```
C:\Users\<Tên người dùng>\.codex\skills\revit-csharp-addin\
```

### Cài cho Claude Code

Cài riêng trong project:
```
<project>\.claude\skills\revit-csharp-addin\
```

Hoặc cài global:
```
C:\Users\<Tên người dùng>\.claude\skills\revit-csharp-addin\
```

### Cài cho Gemini / Antigravity

Cài riêng trong project:
```
<project>\.agents\skills\revit-csharp-addin\
```

Hoặc cài global cho Antigravity:
```
C:\Users\<Tên người dùng>\.gemini\antigravity\skills\revit-csharp-addin\
```

### Sau khi cài

Đóng và mở lại Codex, Claude Code hoặc Antigravity để AI nhận Skill mới.

Sau đó, bạn chỉ cần nhập yêu cầu như:

> Sử dụng Revit C# Skill để tạo plugin có giao diện nhập thông số và tự động dựng mô hình trong Revit.

AI sẽ đọc toàn bộ hướng dẫn trong Skill để viết Revit API đúng cấu trúc, sử dụng Transaction, ExternalEvent, chuyển đổi đơn vị và hỗ trợ nhiều phiên bản Revit tốt hơn.

**Tóm tắt đường dẫn:**

```
Codex              → .agents\skills\revit-csharp-addin
Claude Code        → .claude\skills\revit-csharp-addin
Gemini/Antigravity → .agents\skills\revit-csharp-addin
```

### Link tải
- [Tải Skill for Revit Plugin C# tại đây](https://lenote.dev/shared/docs/skill-for-revit-plugin-cshap)
