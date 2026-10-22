---
name: autocad-drafter
description: >-
  Chuyên gia kỹ sư AI vẽ AutoCAD tự động và triển khai bản vẽ kỹ thuật trong Antigravity.
  Kích hoạt khi người dùng yêu cầu: vẽ bản vẽ AutoCAD (mặt bằng, kiến trúc, kết cấu, nhà thép, móng, dầm, cột, lưới trục),
  điều khiển AutoCAD qua AutoCAD MCP Server, viết code AutoLISP chuẩn kỹ sư, tạo plugin AutoCAD C# .NET,
  hoặc sửa lỗi và tối ưu hóa quy trình CAD Automation.
---

# Kỹ Sư AI Vẽ AutoCAD Tự Động (AutoCAD Drafter Agent Skill)

Skill này hệ thống hóa toàn bộ phương pháp luận, quy trình kỹ thuật 8 bước, tư duy tự kiểm tra và bộ quy tắc nghề nghiệp để AI vận hành như một kỹ sư CAD chuyên nghiệp trong Google Antigravity.

---

## 1. NGUYÊN TẮC CỐT LÕI (AI CAD MINDSET)

1. **Thăm dò trước, cam kết sau (Probe before commit):**
   - Không vội vàng vẽ toàn bộ ngay khi nhận yêu cầu.
   - Luôn kiểm tra môi trường kết nối, kiểm tra tính khả dụng của AutoCAD MCP hoặc kênh LISP trước.
2. **Kịch bản hóa theo tầng (Scripting over Tool Blasting):**
   - Hạn chế tối đa việc bắn từng lệnh đơn lẻ qua socket/pipe.
   - Thay vào đó: Gom các nhóm đối tượng thành kịch bản AutoLISP (`.lsp`) sạch sẽ, nạp theo từng layer độc lập. Điều này giúp dễ debug, có thể tái sử dụng và kiểm soát được lịch sử vẽ.
3. **Tuân thủ thứ tự dựng hình kỹ thuật (Technical Layer Sequence):**
   - Bắt buộc vẽ theo trình tự chuẩn: Lưới trục $\rightarrow$ Cấu kiện chịu lực $\rightarrow$ Tường bao/ngăn $\rightarrow$ Lỗ mở $\rightarrow$ Chi tiết/Nội thất $\rightarrow$ Kích thước (Dim) & Chữ (Text).
4. **Vòng lặp đối chiếu thị giác (Visual Verification Loop):**
   - Lệnh báo "OK" không đồng nghĩa với hình vẽ đúng.
   - Luôn chụp viewport hoặc kiểm tra tọa độ giao điểm đối chiếu lại với yêu cầu/ảnh mẫu.
5. **Cơ chế phục hồi sự cố đa tầng (Multi-tier Fallbacks):**
   - Luôn chuẩn bị sẵn các phương án thay thế: MCP lỗi $\rightarrow$ Nạp file LISP trực tiếp $\rightarrow$ Xuất DXF ngoài qua Python `ezdxf`.
6. **Minh bạch về đánh đổi (Transparent Trade-offs):**
   - Mọi giả định hình học (lệch trục, bo góc, dung sai cột) phải được ghi rõ trong báo cáo kỹ thuật.

---

## 2. QUY TRÌNH 8 BƯỚC TRIỂN KHAI BẢN VẼ

### Bước 1: Làm rõ phạm vi & Thiết lập Ma trận Tọa độ
- Xác nhận đơn vị: Mặc định luôn là **Milimét (mm)**, tỷ lệ 1:1 trong Model Space.
- Xác định quy mô: Kích thước phủ bì $X \times Y$, khoảng cách các bước gian (Spans).
- Lập **Bảng ma trận tọa độ lưới trục (Coordinate Matrix)**:
  - Trục chữ cái (X): A, B, C... kèm tọa độ X tích lũy.
  - Trục số (Y): 1, 2, 3... kèm tọa độ Y tích lũy.
  - Tọa độ các điểm giao nhau (Intersections).

### Bước 2: Kiểm tra kết nối & Phép thử tí hon (Sanity Test)
- Nếu dùng AutoCAD MCP qua socket:
  - Thử nghiệm 1: Gửi lệnh LISP đơn giản: `(+ 1 2)`.
  - Thử nghiệm 2: Nạp thử một routine nhỏ từ file: `(+ 40 2)`.
- Xác định kênh truyền lệnh ổn định nhất cho phiên làm việc.

### Bước 3: Chuẩn bị hệ thống Layer theo tiêu chuẩn
Khởi tạo danh sách Layer với màu sắc (ACI) và LineType rõ ràng:

| Tên Layer | Màu (ACI) | LineType | Đối tượng gán |
|---|---|---|---|
| `0_GRID` | 1 (Đỏ) hoặc 8 (Xám) | CENTER | Lưới trục tim |
| `0_COLUMN` | 4 (Cyan) hoặc 2 (Vàng) | Continuous | Cột BTCT, cột thép |
| `0_WALL_EXT` | 3 (Xanh lá) hoặc 7 | Continuous | Tường bao ngoài |
| `0_WALL_INT` | 2 (Vàng) | Continuous | Tường ngăn chia phòng |
| `0_OPENINGS` | 4 (Cyan) | Continuous | Cửa đi, cửa sổ |
| `0_STAIRS` | 6 (Magenta) | Continuous | Bậc thang, lan can |
| `0_FURNITURE` | 8 (Xám nhạt) | Continuous | Nội thất, thiết bị vệ sinh |
| `0_DIM` | 7 (Trắng/Đen) | Continuous | Kích thước chuỗi và tổng thể |
| `0_TEXT` | 7 (Trắng/Đen) | Continuous | Tên phòng, cao độ, ghi chú |

### Bước 4: Khởi tạo Lưới trục (Grid System)
- Vẽ các đường tim trục từ điểm gốc `(0, 0)`.
- Tự động kéo dài 2 đầu trục một khoảng `extensional space` (mặc định 1000 - 1500mm).
- Vẽ bong bóng trục (Circle bán kính 400 - 600mm) và gán nhãn Text trục tương ứng.

### Bước 5: Dựng Cấu kiện chính & Tường
- **Cột:** Đặt tại các giao điểm trục theo đúng tiết diện (ví dụ: $220 \times 220$ hoặc $300 \times 300$). Tim cột trùng giao điểm hoặc căn theo mép ngoài tường.
- **Tường:** Dùng lệnh Polyline khép kín hoặc Mline, offset từ tim trục ra 2 bên (ví dụ tường 220mm $\rightarrow$ offset mỗi bên 110mm; tường 110mm $\rightarrow$ offset 55mm).
- **Khoét lỗ cửa:** Trích xuất lỗ mở cửa, gắn block cửa hoặc ký hiệu cung tròn góc mở $90^\circ$.

### Bước 6: Hoàn thiện Chi tiết, Nội thất & Cầu thang
- Bố trí các block thiết bị vệ sinh, bồn rửa, bàn ghế (sử dụng block chuẩn hoặc ký hiệu hình học cơ bản).
- Dựng cầu thang: Vẽ các đường bậc cách nhau $250 - 300\text{ mm}$, mũi tên chỉ hướng đi lên (UP).

### Bước 7: Ghi kích thước (Dimension) & Ghi chú (Annotation)
- Bố trí Dim theo nguyên tắc 3 lớp từ trong ra ngoài:
  - **Lớp 1 (Trong cùng):** Dim chi tiết cửa, mảng tường, cột.
  - **Lớp 2 (Giữa):** Dim khoảng cách giữa các trục tim.
  - **Lớp 3 (Ngoài cùng):** Dim kích thước tổng thể toàn công trình.
- Đặt tên phòng, diện tích phòng và cao độ sàn ($\pm 0.000$).

### Bước 8: Kiểm tra, Tự sửa lỗi & Xuất bản vẽ
- Kiểm tra tính khép kín của đường bao tường.
- Kiểm tra khoảng cách Dim không bị đè chữ (Text Overlap).
- **Xuất bản vẽ:**
  - Qua lệnh MCP Plot hoặc `DXFOUT`.
  - Nếu xuất PDF gặp lỗi nền trắng làm mất layer màu trắng (ACI 7): tự động map màu sang TrueColor Black `(0,0,0)` trước khi render.
  - Nếu kết nối MCP gián đoạn: chuyển sang render vector DXF bằng Python `ezdxf` + `matplotlib`.

---

## 3. TIÊU CHUẨN VIẾT MÃ AUTOLISP CHUẨN KỸ SƯ

Khi sinh mã AutoLISP cho AutoCAD, phải luôn áp dụng các nguyên tắc sau:

```lisp
;; ==========================================================================
;; Routine: C:MAKE_GRID_STANDARD
;; Author: Antigravity AutoCAD Specialist
;; ==========================================================================
(defun c:MAKE_GRID_STANDARD ( / *error* oldEcho oldOsm pOrigin xSpans ySpans ext)
  ;; 1. Local error handler
  (defun *error* (msg)
    (if oldEcho (setvar "CMDECHO" oldEcho))
    (if oldOsm (setvar "OSMODE" oldOsm))
    (if (and msg (not (wcmatch (strcase msg) "*BREAK*,*CANCEL*,*QUIT*")))
      (princ (strcat "\n[Lỗi LISP]: " msg))
    )
    (princ)
  )

  ;; 2. Lưu trạng thái hệ thống
  (setq oldEcho (getvar "CMDECHO"))
  (setq oldOsm  (getvar "OSMODE"))
  (setvar "CMDECHO" 0)
  (setvar "OSMODE" 0) ; Tắt bắt điểm khi vẽ tự động để tránh lệch tọa độ

  ;; 3. Thực thi logic vẽ
  ;; ... [Code dựng hình] ...

  ;; 4. Phục hồi trạng thái hệ thống
  (setvar "OSMODE" oldOsm)
  (setvar "CMDECHO" oldEcho)
  (princ "\n[Thành công]: Đã hoàn thành bản vẽ.")
  (princ)
)
```

### Quy tắc quan trọng:
1. **Luôn khai báo Local Variables** sau dấu gạch chéo `( / *error* oldEcho oldOsm ...)`.
2. **Luôn tắt `OSMODE`** (Object Snap) trong quá trình vẽ tự động để tọa độ không bị bắt dính sai lệch vào các điểm lân cận.
3. **Phân biệt phiên bản AutoCAD:**
   - **AutoCAD LT:** Chỉ dùng hàm LISP thuần (`command`, `entmake`, `ssget`), không dùng Visual LISP / COM / ActiveX.
   - **AutoCAD Full:** Có thể dùng thêm các hàm Visual LISP cao cấp (`vlax-*`, `vla-*`, `vl-load-com`).

---

## 4. TÍCH HỢP AUTOCAD MCP SERVER TRONG ANTIGRAVITY

Cấu hình MCP chuẩn trong Antigravity (`~/.gemini/antigravity/mcp_config.json` hoặc workspace config):

```json
{
  "mcpServers": {
    "autocad-mcp": {
      "command": "python",
      "args": ["-m", "autocad_mcp"],
      "env": {
        "AUTOCAD_MCP_BACKEND": "auto"
      }
    }
  }
}
```

### Quy trình kết nối thực tế trong AutoCAD:
1. Mở AutoCAD LT / Full trên Windows.
2. Gõ lệnh `APPLOAD` $\rightarrow$ nạp file `mcp_dispatch.lsp`.
3. Gõ lệnh `MCP_START` để kích hoạt vòng lặp IPC lắng nghe lệnh từ Antigravity.
4. Trong Antigravity, gọi các tool MCP tương ứng (`make_grid`, `add_griddim`, `query_entities`...).
