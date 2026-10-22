# Phân tích hành vi của Claude Opus 4.8 qua bài test vẽ AutoCAD

- **URL:** https://lenote.dev/article/phan-tich-hanh-vi-cua-claude-opus-48-qua-bai-test-ve-autocad
- **Tác giả:** KS 4.0 Academy (@ks40m)
- **Ngày xuất bản:** 2026-05-29 (07:26:07 UTC)
- **Ngày cập nhật:** 2026-10-20 (07:51:16 UTC)
- **Chuyên mục:** Lập trình & AI
- **Từ khóa:** AI, AutoCAD, Claude Opus 4.8, AutoCAD MCP
- **Ảnh bìa:** https://lenotestore.blob.core.windows.net/uploads/images/1780037893510-5vv7zz.webp

---

## Tóm tắt
Trong bài viết này mình sẽ phân tích hành vi của Claude Opus 4.8 qua bài test vẽ AutoCAD, từ cách hiểu yêu cầu, suy luận hình học, lập kế hoạch dựng hình đến khả năng tự sửa lỗi. Qua đó đánh giá mức độ phù hợp của AI trong các tác vụ CAD và kỹ thuật thực tế.

---

## Nội dung bài viết

Một case study về cách Claude Opus 4.8 ra quyết định, tự kiểm tra, và phục hồi khi công cụ hỏng — trong tác vụ vẽ một mặt bằng kết cấu hoàn chỉnh qua AutoCAD MCP.

Nhiệm vụ: cho **Claude Opus 4.8 - trong CoWork** một ảnh bản vẽ mặt bằng và yêu cầu nó dựng lại trong AutoCAD — lưới trục, tường, cột, cửa, cầu thang, nội thất, thiết bị vệ sinh, nhãn, kích thước, rồi xuất file.

![Hình ảnh bản vẽ mặt bằng sử dụng trong bài test này](https://lenotestore.blob.core.windows.net/uploads/images/1780038733057-mksj55.webp)

Điều đáng phân tích không phải là **kết quả** (bản vẽ ra được), mà là **chuỗi quyết định** dẫn tới kết quả đó.

Một kỹ sư mới vào nghề và một kỹ sư lâu năm có thể cùng vẽ ra một bản giống nhau, nhưng cách họ tiếp cận bài toán — thử nghiệm trước hay lao vào làm ngay, kiểm tra bằng mắt hay tin tưởng mù quáng, vá lỗi tạm hay truy nguyên nhân gốc — mới là thứ phân biệt trình độ.

**Kết quả bản vẽ mà Claude Opus 4.8 tạo ra**

![Bản vẽ mà Cladue Opus 4.8 tạo ra](https://lenotestore.blob.core.windows.net/uploads/images/1780038906992-hjh6ci.webp)

**Workspace của Claude Cowork**

![Screenshot 2026-05-29 154032.png](https://lenotestore.blob.core.windows.net/uploads/images/1780039023537-yi2vqn.webp)

**Đánh giá của mình về Claude Opus 4.8**

> Trước đó mình đã thử nhiều mô hình khác như Gemini 3.5 Flash, Gemini 3.1 Pro và Claude Opus 4.5. Tuy nhiên, Claude Opus 4.8 là mô hình mang lại cảm giác tin cậy nhất trong bài test này. Nó không chỉ thực hiện từng bước vẽ một cách cẩn thận mà còn liên tục tự kiểm tra kết quả, phát hiện sai lệch và chủ động điều chỉnh khi cần.
> Một điểm rất thú vị là Claude Opus 4.8 làm được điều mà mình chưa từng thấy ở các mô hình trước đây: thay vì chỉ gửi liên tục các lệnh cho AutoCAD, nó chủ động viết những đoạn AutoLISP nhỏ để tự động hóa các thao tác lặp lại. Thậm chí, trong một số tình huống, nó còn tự tạo các script Python để kiểm tra và xác thực kết quả trước khi tiếp tục thực hiện bước tiếp theo.

Bài này mổ xẻ tám bước của quy trình, nhưng trọng tâm là **vì sao** Claude Opus 4.8 chọn làm như vậy ở mỗi điểm rẽ.

## Phần 1: Quy trình tám bước

### Bước 1 — Làm rõ phạm vi trước khi bắt tay

Thay vì đoán ý người dùng và lao vào vẽ, Claude Opus 4.8 hỏi hai câu cụ thể: mức độ chi tiết mong muốn, và có cần dựng chuỗi kích thước/trục hay không.

Đây là một lựa chọn ngược với bản năng "tỏ ra hữu ích bằng cách làm ngay". Chi phí của hai câu hỏi là vài giây; chi phí của việc đoán sai hướng là vẽ xong cả bản rồi phải làm lại. Agent chọn trả giá phần rẻ.

### Bước 2 — Kiểm tra kết nối + hai phép thử tí hon

Trước khi đầu tư công sức, Claude Opus 4.8 chạy hai phép thử nhỏ để xác định **đường thực thi đáng tin nhất**:

- `(+ 1 2)` qua lệnh LISP trực tiếp.
- `(+ 40 2)` qua việc nạp một file `.lsp`.

Mục đích không phải kiểm tra phép cộng — mà kiểm tra **kênh truyền lệnh**. Hai phép thử này trả lời câu hỏi: gửi lệnh trực tiếp đáng tin, hay ghi ra file rồi để AutoCAD nạp đáng tin hơn? Đây là điểm bản lề của toàn bộ phiên làm việc (sẽ nói kỹ ở phần 2).

### Bước 3 — Chọn chiến lược thực thi

Kết quả phép thử cho thấy: ghi file `.lsp` rồi nạp qua dispatcher ổn định hơn nhiều so với bắn từng lệnh qua socket/pipe. Agent quyết định:

- Toàn bộ hình học sẽ được sinh thành mã nguồn AutoLISP.
- Chia nhỏ thành từng file theo từng tầng dữ liệu.
- Nạp tuần tự và kiểm tra sau mỗi lần nạp.

### Bước 4 — Lập bảng toạ độ từ ảnh mờ

Ảnh đầu vào có chất lượng trung bình, nhiều kích thước bị mờ. Agent không đoán mò các con số lẻ; nó lập bảng ma trận toạ độ lưới trục trước, dùng quan hệ hình học ràng buộc để suy luận kích thước bị thiếu, và ghi rõ các giả định vào một file Markdown riêng trước khi vẽ.

### Bước 5 — Dựng hình theo lớp

Thứ tự dựng hình:
1. Lưới trục + Bong bóng tên trục
2. Cột bê tông cốt thép
3. Tường bao + Tường ngăn (tự động offset từ tim trục)
4. Khoét lỗ cửa đi, cửa sổ
5. Block cầu thang và thiết bị
6. Kích thước chuỗi và nhãn phòng

### Bước 6 — Vòng lặp đối chiếu bằng thị giác máy tính

Sau mỗi lớp hình học được nạp vào AutoCAD, agent ra lệnh chụp ảnh màn hình khung nhìn CAD (viewport capture), sau đó tự gọi mô hình thị giác để so sánh ảnh CAD vừa vẽ với ảnh gốc. Nếu lệch vị trí, agent tính toán vector sai lệch và nạp lệnh bù toạ độ ngay lập tức.

### Bước 7 — Xử lý sự cố xuất file

Khi dùng lệnh plot PDF tiêu chuẩn của CAD qua MCP bị treo, Claude Opus 4.8 đã tự động chuyển hướng: xuất bản vẽ ra dạng DXF, sau đó dùng thư viện `ezdxf` cùng `matplotlib` trong Python ở môi trường ngoài để render ra bản vẽ chuẩn xác.

### Bước 8 — Đóng gói và báo cáo

Agent tổng hợp danh sách các layer đã tạo, toạ độ các cấu kiện chính, các giả định đã đưa ra và xuất file hoàn chỉnh bàn giao cho người dùng.

---

## Phần 2: Những điểm ra quyết định đáng chú ý

Đây là phần thú vị hơn quy trình. Tám bước trên là *cái* Claude Opus 4.8 làm; phần này là *cách nó nghĩ*.

### 2.1 — Thử trước, cam kết sau

Hai phép thử LISP ở bước 2 là điểm bản lề của cả phiên. Trước chúng, mặc định hợp lý là "gọi tool MCP cho từng nét vẽ". Sau chúng, chiến lược đổi hẳn sang "viết một script sạch, kiểm tra được".

Một quyết định nhỏ ở đầu — tốn chưa tới một phút — định hình toàn bộ kiến trúc còn lại. Đây là dấu hiệu của một mô hình biết rằng **chi phí chọn sai đường lớn hơn nhiều chi phí thăm dò**.

### 2.2 — Ưu tiên độ tin cậy và khả năng đọc lại hơn tốc độ

Cách "gọi tool từng nét" có thể cho ra kết quả ngay những nét đầu, tạo cảm giác tiến triển. Nhưng nó mong manh: đứt kết nối giữa chừng là mất hết, và không ai đọc lại được "đã vẽ gì". Script AutoLISP thì chậm khởi động hơn nhưng bền, lặp lại được, và con người đọc hiểu được.

Agent chọn cái chậm-mà-chắc. Đây là một đánh đổi trưởng thành, không phải lựa chọn của người mới.

### 2.3 — Vòng lặp dựng → chụp → đối chiếu

Claude Opus 4.8 không tin "lệnh chạy thành công" là đủ. Nó xác minh bằng hình ảnh thật ở từng mốc. Trong môi trường mà một lệnh có thể "thành công" về mặt cú pháp nhưng vẽ sai vị trí, đây là sự khác biệt giữa một agent *tưởng mình đúng* và một agent *biết mình đúng*.

### 2.4 — Phục hồi khi công cụ hỏng: ít nhất ba lần đổi hướng

Một phiên làm việc thực tế hiếm khi suôn sẻ. Agent gặp và vượt qua ba điểm gãy:

- **DXF**: lệnh MCP lỗi → dùng lệnh `DXFOUT` trực tiếp.
- **PDF**: plot treo → render ngoài bằng thư viện Python.
- **Đồng bộ file giữa hai môi trường**: ghi file thẳng trong sandbox bằng heredoc.

Điểm đáng chú ý không phải là "có lỗi", mà là Claude Opus 4.8 **không bỏ cuộc và không lặp lại đường đã hỏng** — mỗi lần nó tìm một lối khác.

### 2.5 — Gỡ lỗi theo nguyên nhân gốc, không vá bừa

Ví dụ điển hình: tường và chữ "biến mất" trên nền trắng. Một cách vá bừa là đổi màu lung tung cho đến khi thấy. Agent thay vào đó suy luận: AutoCAD lưu nền model màu đen, nên màu ACI 7 ánh xạ thành **trắng** — và trên nền xuất trắng thì trắng-trên-trắng tất nhiên vô hình. Cách sửa: ép các layer đó thành màu đen thật.

Đây là tư duy chẩn đoán: tìm *vì sao* hỏng, không chỉ *làm sao cho hết hỏng*.

### 2.6 — Đánh đổi minh bạch

Khi chốt quy ước "đặt cột giữa trục" để bản vẽ nhất quán nội bộ, Claude Opus 4.8 **nói rõ với người dùng** rằng điều này tạo sai lệch ~100mm so với con số gốc trong ảnh — thay vì giấu đi để bản vẽ trông "khớp hoàn hảo".

Một agent kém trung thực sẽ che mâu thuẫn để trông giỏi hơn. Agent này phơi bày đánh đổi để người dùng tự quyết.

---

## Phần 3: Đọng lại gì cho người xây dựng AI agent?

Nếu rút ra vài nguyên tắc hành vi từ phiên làm việc này:

1. **Thăm dò rẻ thì thăm dò trước.** Một phép thử nhỏ ở đầu có thể đổi hướng cả kiến trúc, và nó luôn rẻ hơn việc làm lại.
2. **"Không báo lỗi" không phải là "đúng".** Phải có vòng xác minh độc lập — ở đây là ảnh chụp đối chiếu.
3. **Độ bền và khả năng đọc lại thường đáng giá hơn tốc độ tức thời** trong tác vụ dài hơi.
4. **Gặp tường thì đi vòng, đừng đập đầu.** Có sẵn nhiều lối thoát (fallback) là dấu hiệu của thiết kế tốt.
5. **Chẩn đoán nguyên nhân gốc** tiết kiệm hơn vá triệu chứng về lâu dài.
6. **Minh bạch về đánh đổi** xây niềm tin tốt hơn là tỏ ra hoàn hảo.

Những nguyên tắc này không riêng cho AutoCAD. Chúng áp dụng cho bất kỳ agent nào phải hành động trong một môi trường thực — nơi công cụ hỏng, dữ liệu mâu thuẫn, và "có vẻ chạy" không đồng nghĩa với "chạy đúng".
