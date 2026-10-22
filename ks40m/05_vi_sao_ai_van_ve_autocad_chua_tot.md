# Vì sao AI vẫn vẽ AutoCAD chưa tốt?

- **URL:** https://lenote.dev/article/vi-sao-ai-van-ve-autocad-chua-tot
- **Tác giả:** KS 4.0 Academy (@ks40m)
- **Ngày xuất bản:** 2026-05-18 (01:08:43 UTC)
- **Ngày cập nhật:** 2026-10-21 (01:59:37 UTC)
- **Chuyên mục:** Lập trình & AI
- **Từ khóa:** AGENT SKILL, AI, AutoCAD, AutoCAD MCP
- **Thời lượng:** 5 phút đọc
- **Ảnh bìa:** https://lenotestore.blob.core.windows.net/uploads/images/1779066445484-ruorwe.webp

---

## Tóm tắt
Bài viết này sẽ giải thích vì sao AI hiện tại vẫn chưa thể vẽ AutoCAD tốt chỉ bằng prompt, và cách AI Agent, MCP, Skill cùng các tool chuyên biệt đang giúp AI làm việc giống một kỹ sư CAD thật.

---

## Nội dung bài viết

Nhiều người nghĩ chỉ cần sử dụng các mô hình ngôn ngữ lớn như:

- **ChatGPT**
- **Claude**
- **Gemini**

là có thể tự động vẽ AutoCAD hoàn hảo. Nhưng thực tế không đơn giản như vậy.

## Vấn đề lớn nhất của AI hiện tại

AI thông thường hiện nay chỉ giỏi trong các tác vụ:

- Trả lời câu hỏi
- Viết code
- Tạo nội dung

Nhưng một **bản vẽ kỹ thuật** lại đòi hỏi khắt khe về:

- Logic hình học và không gian
- Workflow (quy trình làm việc) nghiêm ngạc
- Quy tắc đặc thù của từng ngành nghề
- Khả năng kiểm tra lỗi (Double-check)
- Thao tác trực tiếp trên phần mềm thật

Đây là lý do vì sao khi đụng đến CAD, AI rất dễ gặp tình trạng:

- **Hallucination** (ảo tưởng, tự bịa ra dữ liệu)
- Vẽ sai tỷ lệ, vị trí
- Thiếu đối tượng quan trọng
- Dim (ghi kích thước) sai mục tiêu
- Layer lộn xộn, không theo chuẩn
- Mất tính logic tổng thể của bản vẽ

## Điều AI thiếu không phải “thông minh”

Cái AI đang thiếu không phải là chỉ số thông minh (IQ), mà là:

- **Công cụ** kết nối chuyên biệt
- **Workflow** thực tế
- **Khả năng thao tác** trên môi trường thật

> **Ví dụ thực tế:** Một kỹ sư CAD thực thụ không bao giờ ngồi vẽ từng đường line một cách ngẫu nhiên. Họ luôn vận hành dựa trên một hệ thống có sẵn gồm: Quy trình rõ ràng, Template chuẩn, Tiêu chuẩn kỹ thuật, Công cụ hỗ trợ và Kinh nghiệm kiểm tra lỗi tích lũy. AI muốn vẽ được cũng cần một hệ thống như vậy.

## AI Agent mới là hướng đi thật sự

AI Agent (Đại lý AI) khác biệt hoàn toàn với các chatbot thông thường ở chỗ:

- Biết sử dụng các công cụ (**tools**) được cung cấp
- Biết thao tác trực tiếp trên phần mềm
- Có khả năng tự kiểm tra kết quả
- Biết sửa lỗi khi phát hiện điểm bất hợp lý
- Biết tuân thủ và chạy theo một workflow tuần tự

### Ví dụ về workflow của một AI Agent

Khi người dùng ra lệnh: *"Vẽ mặt bằng nhà thép"*

AI Agent sẽ tự động triển khai theo các bước:

1. Phân tích yêu cầu và thông số đầu vào.
2. Tạo hệ lưới (Grid).
3. Đặt tên các trục layout.
4. Vẽ hệ thống cột.
5. Vẽ hệ thống dầm kết nối.
6. Ghi kích thước (Dim).
7. Chạy thuật toán kiểm tra lỗi.
8. Nếu phát hiện sai sót, tự động quay lại sửa đổi.

## Muốn AI vẽ AutoCAD tốt hơn cần những gì?

### 1. Kết nối trực tiếp với AutoCAD

AI cần phải có "đôi tay" để thao tác được trên phần mềm thật, thông qua các hành động:

- Gửi command (lệnh) trực tiếp vào CAD.
- Đọc thông tin của các Object (đối tượng).
- Kiểm tra và phân loại Layer.
- Lấy dữ liệu kích thước thực tế.
- Chỉnh sửa trực tiếp trên bản vẽ.

#### MCP là gì?

**MCP (Model Context Protocol)** giống như một chiếc cầu nối kỹ thuật số giữa AI và phần mềm AutoCAD:

```
Claude / ChatGPT / Gemini
        ↓
    AI Agent
        ↓
      MCP
        ↓
   AutoCAD
        ↓
   DWG thật
```

Nhờ có MCP, AI không chỉ dừng lại ở việc "nói" hay "hướng dẫn" suông. Nó có thể trực tiếp: **Thao tác** $\rightarrow$ **Đọc trạng thái** $\rightarrow$ **Chạy workflow thật**.

### 2. Tool chuyên biệt quan trọng hơn prompt

Nhiều người vẫn đang ra lệnh cho AI một cách quá mơ hồ: *"Vẽ cho tôi bản vẽ AutoCAD"*.

Thay vào đó, hệ thống cần cung cấp cho AI các **Tool chuyên biệt** như:

- `MAKE_GRID`: Tạo lưới trục
- `TAG_GRID`: Đánh nhãn trục
- `DRAW_COLUMN`: Vẽ cột
- `DRAW_BEAM`: Vẽ dầm
- `DIM_GRID`: Dim kích thước lưới
- `CHECK_DRAWING`: Kiểm tra bản vẽ

Lúc này, AI chỉ cần thực hiện 3 bước đơn giản: **Hiểu yêu cầu** $\rightarrow$ **Chọn đúng tool** $\rightarrow$ **Thực hiện đúng workflow**.

### 3. Skill (Kỹ năng) giúp AI hiểu ngành xây dựng

**Skill** ở đây chính là bộ kiến thức nghiệp vụ được đóng gói dành riêng cho AI, bao gồm:

- Quy tắc tạo trục và bố trí layout.
- Quy tắc đặt đường Dim (không chồng chéo, rõ ràng).
- Quy tắc quản lý và phân loại Layer.
- Quy tắc sử dụng Text (font, tỷ lệ, chiều cao).
- Các tiêu chuẩn thiết kế bản vẽ hiện hành.
- Quy tắc hậu kiểm và phát hiện lỗi kỹ thuật.
- **Không có skill:** AI chỉ là một chatbot tổng quát, nói lý thuyết suông.
- **Có skill:** AI bắt đầu tư duy và làm việc giống như một nhân sự CAD thực thụ.

## Tương lai của AI trong AutoCAD

Tương lai của thiết kế kỹ thuật không phải là việc AI tự động vẽ ra mọi thứ chỉ bằng một câu prompt ngắn ngủi. Nó sẽ là kỷ nguyên của các **AI Agent** biết sử dụng thành thạo công cụ (Tool), có kiến thức chuyên môn (Skill) và tuân thủ quy trình (Workflow) y như một kỹ sư thật sự.

### Điều quan trọng nhất

Để nâng cấp năng lực vẽ AutoCAD của AI, việc nâng cấp các model (GPT-5, Claude 4...) là chưa đủ. Yếu tố cốt lõi nằm ở hệ sinh thái xung quanh nó:

> **AI Tiến Hóa = AI Agent + MCP + Skill + Tool chuyên biệt + Workflow rõ ràng + Cơ chế tự sửa lỗi**

> **Câu chốt:** Một AI mạnh chưa chắc đã vẽ CAD tốt. Nhưng một AI được trang bị **Agent + MCP + Skill + Tool đúng** chắc chắn sẽ bắt đầu làm việc hiệu quả như một kỹ sư CAD thực thụ.
