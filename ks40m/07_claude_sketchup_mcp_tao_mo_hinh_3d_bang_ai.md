# Claude + SketchUp MCP: Tạo mô hình 3D bằng AI?

- **URL:** https://lenote.dev/article/claude-sketchup-mcp-tao-mo-hinh-3d-bang-ai
- **Tác giả:** KS 4.0 Academy (@ks40m)
- **Ngày xuất bản:** 2026-05-11 (09:09:35 UTC)
- **Ngày cập nhật:** 2026-10-20 (12:38:57 UTC)
- **Chuyên mục:** Lập trình & AI
- **Từ khóa:** Claude, Generative AI, SketchUp
- **Thời lượng:** 8 phút đọc
- **Ảnh bìa:** https://lenotestore.blob.core.windows.net/uploads/images/1778484275725-nf6u3o.webp

---

## Tóm tắt
Trong bài này mình sẽ hướng dẫn các bạn cách kết nối Claude Desktop với SketchUp một cách chi tiết, đồng thời demo nhanh cách sử dụng để mọi người dễ hình dung hơn.

---

## Nội dung bài viết

SketchUp là phần mềm cho phép mô hình hóa nhà cửa và không gian 3D một cách dễ dàng. Đặc biệt, nó được sử dụng rất phổ biến trong các lĩnh vực như kiến trúc, nội thất và thiết kế sản phẩm.

Năm 2006, Google đã mua lại Last Software — công ty phát triển ban đầu của SketchUp — và phát hành phiên bản miễn phí với tên gọi “Google SketchUp”, nhờ đó phần mềm nhanh chóng trở nên phổ biến.

Sau đó, vào năm 2012, Trimble Inc. tiếp tục mua lại SketchUp. Từ đó đến nay, các phiên bản hiện tại của SketchUp, bao gồm cả bản Web, đều được phát triển và cung cấp bởi Trimble.

“Trimble SketchUp Connector” tương thích với Claude của Anthropic là một MCP Server do Trimble Inc. cung cấp, và có thể sử dụng bằng cách kích hoạt nó từ thư mục MCP của Claude.

Để sử dụng, cần có tài khoản Claude và Trimble ID, sau đó tiến hành xác thực để kết nối.

SketchUp Connector thuộc kiểu “hand-off” (bàn giao). Tức là Claude sẽ tạo phần khởi đầu của mô hình từ đoạn chat, sau đó người dùng hoàn thiện tiếp trong giao diện SketchUp.

Nó khác với kiểu “Agentic” như Blender hay Autodesk Fusion — nơi AI có thể trực tiếp thao tác các object bên trong ứng dụng theo thời gian thực.

# Cài đặt SketchUp MCP

Việc kết nối **SketchUp MCP** cực kỳ đơn giản.

Về cơ bản, bạn chỉ cần vào phần connectors trong **Customize** của **Claude Desktop**, tìm **SketchUp** của **Trimble Inc**. rồi nhấn nút “Liên kết / Kết nối” là xong.

Sau đó, chỉ cần nhập tài khoản của **Trimble Inc.** là quá trình thiết lập sẽ hoàn tất.

# Làm sao để sử dụng?

**SketchUp MCP** là dạng “hand-off”, người dùng không cần phải mở SketchUp trên máy tính local.

Claude sẽ tạo dữ liệu 3D ở định dạng SketchUp trên cloud và xuất ra dưới dạng file .skp, chứ không trực tiếp thao tác SketchUp trên PC của người dùng.

Tiếp theo, hãy thử tạo một mô hình kiến trúc đơn giản với nội dung như sau:

```
Bạn là một AI hỗ trợ tạo mô hình kiến trúc trong SketchUp.

Hãy tạo một mô hình công trình kiến trúc đơn giản theo các yêu cầu sau:

* Kích thước công trình: rộng 10.000mm × dài 15.000mm
* Công trình gồm 1 tầng
* Chiều cao tầng: 3.500mm
* Hệ mái: mái bằng
* Tường parapet bao quanh mái cao 300mm

Yêu cầu mặt đứng:

* Cửa chính đặt tại trung tâm mặt đứng phía Nam
* Kích thước cửa chính: 1.000mm × 2.100mm

Cửa sổ:

* Bố trí đều trên mặt đứng phía Nam và phía Bắc
* Kích thước mỗi cửa sổ: 1.200mm × 1.500mm
* Cao độ bệ cửa sổ: 900mm

Yêu cầu mô hình:

* Sử dụng đơn vị milimét (mm)
* Mô hình phải sạch, dễ chỉnh sửa
* Các thành phần nên được group hợp lý
* Không cần vật liệu hoặc render phức tạp
* Xuất ra file `.skp` có thể mở và chỉnh sửa trực tiếp trong SketchUp
```

# Tóm tắt mô hình SketchUp đã tạo

**File:** `kani_1tang_10x15.skp`

### Quy đổi đơn vị

SDK SketchUp dùng inch, nên toàn bộ kích thước mm được quy đổi qua hệ số `MM = 1/25.4`. Kết quả file vẫn chính xác theo mm khi đổi đơn vị hiển thị trong SketchUp (Window → Model Info → Units → Millimeters).

### Cấu trúc mô hình (10 groups)

##### Sàn & mái (2 groups)

- `Slab_Floor` — sàn nền 10000×15000mm, dày 150mm, cao độ -150 → 0
- `Slab_Roof` — mái bằng cùng kích thước, cao độ +3500 → +3650

##### Tường bao (4 groups, dày 200mm, cao 3500mm)

- `Wall_South` — có 1 cửa chính + 2 cửa sổ (đã khoét bằng inner loop)
- `Wall_North` — có 3 cửa sổ phân bố đều
- `Wall_East`, `Wall_West` — tường đặc, không lỗ mở

##### Parapet (4 groups, cao 300mm, dày 200mm trên mái)

- `Parapet_South`, `Parapet_North`, `Parapet_East`, `Parapet_West` — 4 đoạn ghép thành vòng kín, không chồng chéo

### Bố trí cửa

| Mặt | Vị trí (tâm theo X) | Loại | Kích thước |
| --- | --- | --- | --- |
| Nam | 2250mm | Cửa sổ | 1200×1500mm, bệ 900mm |
| Nam | 5000mm | Cửa chính | 1000×2100mm |
| Nam | 7750mm | Cửa sổ | 1200×1500mm, bệ 900mm |
| Bắc | 2500mm | Cửa sổ | 1200×1500mm, bệ 900mm |
| Bắc | 5000mm | Cửa sổ | 1200×1500mm, bệ 900mm |
| Bắc | 7500mm | Cửa sổ | 1200×1500mm, bệ 900mm |

### Kỹ thuật quan trọng

- **Inner loop cho mọi lỗ mở** — tường giữ nguyên là một mặt liền, không bị chia mảnh → dễ chỉnh sửa trong SketchUp
- **Jamb/header/sill đầy đủ** — mỗi lỗ mở có 4 mặt phụ khép kín độ dày tường, tường là solid kín
- **Coplanar edge softening** — các cạnh chéo do triangulation đã được set soft+smooth, mặt tường hiển thị phẳng, góc vẫn sắc
- **Group hợp lý theo chức năng** — mỗi cấu kiện một group có tên, dễ chọn và edit độc lập

### Hoàn thiện file

- Camera chéo phía Tây-Nam, FOV 35°, góc nhìn 3D mặc định
- Style đặt tên `Kani_Architectural_Clean`
- Bật bóng đổ nhẹ (Light 70, Dark 45) để mặt đứng có chiều sâu

### Thông số tổng thể

| Hạng mục | Giá trị |
| --- | --- |
| Kích thước công trình | 10000 × 15000mm |
| Chiều cao tầng | 3500mm |
| Số tầng | 1 |
| Hệ mái | Mái bằng + parapet 300mm |
| Độ dày tường | 200mm |
| Độ dày sàn/mái | 150mm |
| Tổng số group | 10 |
| Đơn vị file gốc | Inch (SDK), hiển thị mm trong SketchUp |

# Tổng kết

**SketchUp MCP Connector** mang đến một cách tiếp cận khác biệt so với các AI agent kiểu Blender hay Fusion: thay vì điều khiển phần mềm trên máy local theo thời gian thực, Claude đóng vai trò **"kiến trúc sư khởi tạo"** — dựng sẵn bộ khung mô hình trên cloud, group hóa rõ ràng, và bàn giao file `.skp` sạch để người dùng tiếp tục hoàn thiện trong môi trường quen thuộc của SketchUp.

### Ưu điểm

- **Không cần cài SketchUp trên máy** — phù hợp khi cần phác thảo nhanh trên thiết bị nhẹ hoặc khi đang di chuyển
- **File output có cấu trúc tốt** — group hợp lý, inner loop cho lỗ mở, jamb/header/sill đầy đủ → tiết kiệm thời gian dọn dẹp model
- **Chuyển từ ý tưởng sang khối hình rất nhanh** — chỉ cần prompt mô tả kích thước, công năng, mặt đứng là đã có khung 3D để bắt đầu thiết kế

### Hạn chế

- **Không tương tác real-time** — không thể bảo Claude "kéo tường này lên 500mm" như với Blender MCP. Mọi thay đổi phải tạo lại file từ đầu hoặc chỉnh tay trong SketchUp
- **Không thấy được trực tiếp những gì đang được tạo** — phải đợi xuất file rồi mở ra mới biết kết quả
- **Phù hợp giai đoạn concept hơn là detail design** — vật liệu, render, component phức tạp vẫn cần thao tác thủ công

### Khi nào nên dùng?

SketchUp Connector phát huy giá trị nhất ở **giai đoạn schematic design** — khi cần dựng nhanh nhiều phương án để so sánh, hoặc khi muốn truyền đạt ý tưởng kiến trúc qua mô tả ngôn ngữ tự nhiên thay vì vẽ tay từng đường. Với những công trình đơn giản như nhà 1–2 tầng, nhà phố, hoặc các khối kiến trúc cơ bản, đây là công cụ rất đáng thử.

Còn với những dự án đòi hỏi BIM data chi tiết, phối hợp đa bộ môn, hay quản lý khối lượng — **Revit MCP hoặc AutoCAD MCP vẫn là lựa chọn phù hợp hơn**.

---

Trong tương lai, khi MCP ecosystem của ngành xây dựng phát triển hơn, mình kỳ vọng sẽ có sự kết hợp giữa **hand-off model** (như SketchUp) và **agentic model** (như Blender) — nơi AI vừa có thể khởi tạo nhanh, vừa có thể tinh chỉnh tương tác. Đó mới là điểm chạm thực sự giữa AI và quy trình thiết kế kiến trúc.
