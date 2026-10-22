# -*- coding: utf-8 -*-
"""
Generate comprehensive, professional .docx manual for Brother PS-300C.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

from manual_builder_base import (
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_TEXT, COLOR_MUTED, COLOR_RED, COLOR_GREEN,
    HEX_PRIMARY, HEX_SECONDARY, HEX_LIGHT_BLUE, HEX_LIGHT_GREEN, HEX_LIGHT_AMBER,
    HEX_LIGHT_GRAY, HEX_BORDER, HEX_BORDER_DARK,
    set_cell_background, set_cell_margins, set_table_borders,
    add_header_footer, add_custom_heading, add_body_p, add_bullet_item,
    add_callout, add_figure
)

def create_manual():
    doc = docx.Document()
    add_header_footer(doc)
    
    # ----------------------------------------------------
    # COVER PAGE / BÌA TÀI LIỆU CÔNG NGHIỆP
    # ----------------------------------------------------
    p_org = doc.add_paragraph()
    p_org.paragraph_format.space_before = Pt(12)
    p_org.paragraph_format.space_after = Pt(4)
    r_org = p_org.add_run("BROTHER ASIA INDUSTRIAL SEWING MACHINE")
    r_org.bold = True
    r_org.font.name = "Arial"
    r_org.font.size = Pt(11)
    r_org.font.color.rgb = COLOR_PRIMARY
    
    p_dept = doc.add_paragraph()
    p_dept.paragraph_format.space_after = Pt(28)
    r_dept = p_dept.add_run("BỘ PHẬN NGHIÊN CỨU & CHUYỂN GIAO KỸ THUẬT CÔNG NGHỆ MAY TỰ ĐỘNG")
    r_dept.font.name = "Arial"
    r_dept.font.size = Pt(9.5)
    r_dept.font.color.rgb = COLOR_MUTED
    
    # Banner title
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_after = Pt(8)
    r_t1 = p_title.add_run("TÀI LIỆU HƯỚNG DẪN KỸ THUẬT VÀ LẬP TRÌNH DỮ LIỆU MAY\n")
    r_t1.bold = True
    r_t1.font.name = "Arial"
    r_t1.font.size = Pt(22)
    r_t1.font.color.rgb = COLOR_PRIMARY
    
    r_t2 = p_title.add_run("PHẦN MỀM BROTHER PS-300C\n(SEWING DATA CREATION SOFTWARE)")
    r_t2.bold = True
    r_t2.font.name = "Arial"
    r_t2.font.size = Pt(18)
    r_t2.font.color.rgb = COLOR_SECONDARY
    
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(20)
    r_sub = p_sub.add_run("Chuẩn Mực Thế Hệ Mới: Tối Ưu Hóa Giao Diện, Tích Hợp CAD DXF Hai Chiều, Tự Động Kiểm Soát Chất Lượng, Mô Phỏng Động Học & Tùy Biến Thiết Bị May May Chế")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(11)
    r_sub.italic = True
    r_sub.font.color.rgb = COLOR_TEXT
    
    # Add Banner Picture
    add_figure(doc, "final_screenshots/20_brother_ps300c_official_banner.png", 
               "Hình 1: Brother PS-300C - The Next Standard in Sewing Data Creation (Nguồn chính thức Brother)", width=Inches(6.0))
    
    # Metadata Table
    p_meta_title = doc.add_paragraph()
    p_meta_title.paragraph_format.space_before = Pt(8)
    p_meta_title.paragraph_format.space_after = Pt(4)
    r_mt = p_meta_title.add_run("BẢNG THÔNG TIN KIỂM SOÁT TÀI LIỆU:")
    r_mt.bold = True
    r_mt.font.name = "Arial"
    r_mt.font.size = Pt(9.5)
    r_mt.font.color.rgb = COLOR_SECONDARY
    
    tbl_meta = doc.add_table(rows=6, cols=2)
    tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_meta)
    
    meta_data = [
        ("Tên tài liệu", "Sổ tay Hướng dẫn Kỹ thuật & Vận hành Phần mềm Brother PS-300C"),
        ("Mã tài liệu / Phiên bản", "SOP-ENG-BROTHER-PS300C | Phiên bản 1.0 (Official Standard)"),
        ("Nguồn tư liệu gốc", "Video chính thức: https://www.youtube.com/watch?v=TQseJ2dYmr4 (Điểm nhấn t=146s)"),
        ("Đơn vị ban hành", "Brother Asia Industrial Sewing Machine - Tech Support & Automation Dept"),
        ("Đối tượng áp dụng", "Kỹ sư Rập CAD, Kỹ thuật viên Lập trình máy may tự động, Kỹ sư IE, Bảo trì cơ điện"),
        ("Mục tiêu chuẩn hóa", "Nâng cao 50% tốc độ tạo dữ liệu rập may, triệt tiêu 100% lỗi cài đặt sai hỏng trước khi lên máy")
    ]
    
    col_widths = [Inches(2.2), Inches(4.27)]
    for row_idx, (k, v) in enumerate(meta_data):
        row = tbl_meta.rows[row_idx]
        cell_k, cell_v = row.cells[0], row.cells[1]
        
        cell_k.width = col_widths[0]
        cell_v.width = col_widths[1]
        
        set_cell_background(cell_k, HEX_LIGHT_BLUE)
        set_cell_background(cell_v, "FFFFFF" if row_idx % 2 == 0 else HEX_LIGHT_GRAY)
        set_cell_margins(cell_k, top=100, bottom=100, left=140, right=140)
        set_cell_margins(cell_v, top=100, bottom=100, left=140, right=140)
        
        pk = cell_k.paragraphs[0]
        pk.paragraph_format.space_after = Pt(0)
        rk = pk.add_run(k)
        rk.bold = True
        rk.font.name = "Arial"
        rk.font.size = Pt(9)
        rk.font.color.rgb = COLOR_SECONDARY
        
        pv = cell_v.paragraphs[0]
        pv.paragraph_format.space_after = Pt(0)
        rv = pv.add_run(v)
        rv.font.name = "Arial"
        rv.font.size = Pt(9)
        rv.font.color.rgb = COLOR_TEXT
        
    doc.add_page_break()
    
    # ----------------------------------------------------
    # MỤC LỤC VÀ TỔNG QUAN TÀI LIỆU
    # ----------------------------------------------------
    add_custom_heading(doc, "MỤC LỤC HỆ THỐNG VÀ TỔNG QUAN TÀI LIỆU", level=1)
    
    add_body_p(doc, 
               "Tài liệu này được biên soạn nhằm hệ thống hóa toàn bộ kiến thức, quy trình thao tác và tính năng đột phá của phần mềm Brother PS-300C - thế hệ phần mềm lập trình và tạo dữ liệu may công nghiệp tiên tiến nhất từ tập đoàn Brother. Nội dung được trích xuất trực tiếp và phân tích chuyên sâu từ video công bố chính thức, tập trung giải quyết triệt để các vướng mắc kỹ thuật thực tế tại các nhà máy may may công nghiệp hiện đại.")
    
    # Table of Contents Items
    toc_items = [
        ("Chương 1", "Tổng quan về phần mềm Brother PS-300C & Bối cảnh chuyển đổi công nghệ"),
        ("Chương 2", "Bảng so sánh chuyên sâu: Brother PS-300C vs Thế hệ tiền nhiệm PS-300B"),
        ("Chương 3", "Cấu trúc giao diện người dùng mới (Redesigned UI & Smart Navigation)"),
        ("Chương 4", "Quy trình biên tập và quản lý dữ liệu đường may (Streamlined Workflows)"),
        ("Chương 5", "Bảng tra cứu phím tắt điều khiển toàn diện (Keyboard Shortcuts Cheat Sheet)"),
        ("Chương 6", "Tích hợp và bóc tách bản vẽ CAD định dạng DXF (Enhanced DXF Integration)"),
        ("Chương 7", "Hệ thống kiểm soát chất lượng & Tự động phát hiện lỗi (Quality Verification & Alerts)"),
        ("Chương 8", "Mô phỏng đường may & Dự toán thời gian chu kỳ sản xuất (Playback Simulation & Cycle Time)"),
        ("Chương 9", "Tùy biến thông số thiết bị may theo xưởng sản xuất (Machine Customization - Điểm nhấn t=146s)"),
        ("Chương 10", "Quy trình thực hành tiêu chuẩn SOP 6 bước & Checklist bàn giao tại nhà máy")
    ]
    
    tbl_toc = doc.add_table(rows=len(toc_items) + 1, cols=2)
    tbl_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_toc)
    
    # Header row
    h_cell0, h_cell1 = tbl_toc.rows[0].cells[0], tbl_toc.rows[0].cells[1]
    h_cell0.width = Inches(1.5)
    h_cell1.width = Inches(4.97)
    set_cell_background(h_cell0, HEX_PRIMARY)
    set_cell_background(h_cell1, HEX_PRIMARY)
    set_cell_margins(h_cell0, top=120, bottom=120, left=140, right=140)
    set_cell_margins(h_cell1, top=120, bottom=120, left=140, right=140)
    
    p_h0 = h_cell0.paragraphs[0]
    p_h0.paragraph_format.space_after = Pt(0)
    r_h0 = p_h0.add_run("CHƯƠNG MỤC")
    r_h0.bold = True
    r_h0.font.name = "Arial"
    r_h0.font.size = Pt(9.5)
    r_h0.font.color.rgb = RGBColor(255, 255, 255)
    
    p_h1 = h_cell1.paragraphs[0]
    p_h1.paragraph_format.space_after = Pt(0)
    r_h1 = p_h1.add_run("NỘI DUNG HUẤN LUYỆN & HƯỚNG DẪN KỸ THUẬT")
    r_h1.bold = True
    r_h1.font.name = "Arial"
    r_h1.font.size = Pt(9.5)
    r_h1.font.color.rgb = RGBColor(255, 255, 255)
    
    for idx, (ch, desc) in enumerate(toc_items, start=1):
        row = tbl_toc.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(1.5)
        c1.width = Inches(4.97)
        bg = HEX_LIGHT_BLUE if idx % 2 == 1 else "FFFFFF"
        set_cell_background(c0, bg)
        set_cell_background(c1, bg)
        set_cell_margins(c0, top=100, bottom=100, left=140, right=140)
        set_cell_margins(c1, top=100, bottom=100, left=140, right=140)
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(ch)
        r0.bold = True
        r0.font.name = "Arial"
        r0.font.size = Pt(9)
        r0.font.color.rgb = COLOR_PRIMARY
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(desc)
        r1.font.name = "Arial"
        r1.font.size = Pt(9)
        r1.font.color.rgb = COLOR_TEXT
        
    add_callout(doc, 
                "Tài liệu đặc biệt nhấn mạnh tính năng Tùy biến thông số máy (Machine Customization) tại mốc thời gian t=146s của video. Đây là tính năng then chốt giúp các nhà máy tự do thiết lập vùng may và công nghệ hỗ trợ cho các dòng máy may cải tiến hoặc bàn kẹp khuôn may đặc thù.",
                title="ĐIỂM NHẤN CÔNG NGHỆ (TIMESTAMP T=146S)", box_type="tip")
    
    doc.add_page_break()
    
    # ----------------------------------------------------
    # CHƯƠNG 1: TỔNG QUAN VỀ PHẦN MỀM BROTHER PS-300C
    # ----------------------------------------------------
    add_custom_heading(doc, "CHƯƠNG 1: TỔNG QUAN VỀ PHẦN MỀM BROTHER PS-300C & BỐI CẢNH CÔNG NGHỆ", level=1)
    
    add_custom_heading(doc, "1.1 Bối cảnh ngành công nghiệp may hiện đại", level=2)
    add_body_p(doc, 
               "Trong kỷ nguyên chuyển đổi số và tự động hóa sản xuất ngành may (Garment, Footwear, Bags, Automotive Seating), các nhà máy đang phải đối mặt với những thách thức chưa từng có:")
    
    add_bullet_item(doc, " Chu kỳ sống của sản phẩm ngày càng ngắn, các thương hiệu liên tục thay đổi kiểu dáng và đòi hỏi giao hàng nhanh chóng.", bold_prefix="Áp lực rút ngắn Lead Time:")
    add_bullet_item(doc, " Sự bùng nổ của các đơn hàng nhỏ, đa dạng mẫu mã (High-Mix Low-Volume) đòi hỏi phòng rập và kỹ thuật phải lập trình hàng chục bộ dữ liệu may mới mỗi ngày.", bold_prefix="Đa dạng hóa mẫu mã linh hoạt:")
    add_bullet_item(doc, " Đường may trên máy may lập trình tự động (như Brother BAS Series) đòi hỏi sự chính xác tuyệt đối đến từng 0.1 mm, không cho phép sai lệch gây rách vật liệu, gãy kim hay đứt chỉ.", bold_prefix="Yêu cầu độ chuẩn xác khắt khe:")
    add_bullet_item(doc, " Các nhà máy liên tục cải tiến bàn kẹp (Jig/Clamp) và độ chế máy để đáp ứng các công đoạn may chuyên dụng, nhưng phần mềm cũ không cho phép tùy biến thông số máy.", bold_prefix="Đặc thù thiết bị độ chế và cải tiến:")
    
    add_custom_heading(doc, "1.2 Sự ra đời của Brother PS-300C: The Next Standard", level=2)
    add_body_p(doc, 
               "Để giải quyết triệt để những điểm nghẽn trên, Brother Industrial Sewing Machine đã nghiên cứu và phát triển phần mềm lập trình thế hệ mới mang tên Brother PS-300C. Khẩu hiệu định vị của phần mềm: \"The Next Standard in Sewing Data Creation\" (Chuẩn mực mới trong tạo lập dữ liệu may).")
    
    add_body_p(doc, 
               "Phần mềm được thiết kế dựa trên 3 giá trị cốt lõi:")
    add_bullet_item(doc, " Giao diện phẳng trực quan, tối ưu hóa thao tác người dùng, giúp kỹ thuật viên làm việc nhanh hơn và giảm thiểu mệt mỏi.", bold_prefix="1. Nhanh hơn (Faster):")
    add_bullet_item(doc, " Tích hợp mượt mà bản vẽ CAD DXF, quản lý cây phân đoạn Outline thường trực, thao tác bắt điểm Snap và cuộn Pan tiện lợi.", bold_prefix="2. Đơn giản hơn (Simpler):")
    add_bullet_item(doc, " Tự động phát hiện lỗi cài đặt bất thường, kiểm tra va chạm, mô phỏng chuyển động động học chân thực và tính toán chính xác thời gian chu kỳ may.", bold_prefix="3. Tin cậy hơn (More Reliable):")
    
    # ----------------------------------------------------
    # CHƯƠNG 2: BẢNG SO SÁNH BROTHER PS-300C VS PS-300B
    # ----------------------------------------------------
    add_custom_heading(doc, "CHƯƠNG 2: BẢNG SO SÁNH CHUYÊN SÂU: BROTHER PS-300C VS THẾ HỆ TIỀN NHIỆM PS-300B", level=1)
    
    add_custom_heading(doc, "2.1 Phân tích các hạn chế cố hữu của phần mềm cũ PS-300B", level=2)
    add_body_p(doc, 
               "Thế hệ tiền nhiệm Brother PS-300B từng là công cụ quen thuộc trong các nhà máy may suốt nhiều năm qua. Mặc dù sở hữu nhiều chức năng mạnh mẽ, PS-300B tồn tại nhiều nhược điểm lớn làm suy giảm hiệu suất lao động:")
    
    add_bullet_item(doc, " Giao diện kiểu cũ Windows XP/98 với hàng loạt thanh công cụ nhỏ xíu, biểu tượng dày đặc và menu đa tầng khiến việc tìm kiếm đúng công cụ may vô cùng mất thời gian.", bold_prefix="Giao diện phức tạp, khó tiếp cận:")
    add_bullet_item(doc, " Khi nhập tệp DXF từ phần mềm thiết kế rập CAD, PS-300B nhập toàn bộ các đường nét mà không cho xem trước hoặc lọc bỏ Layer không cần thiết.", bold_prefix="Xử lý CAD DXF thô sơ:")
    add_bullet_item(doc, " Không có hệ thống phát hiện lỗi bước mũi may tự động. Kỹ thuật viên phải kiểm tra thủ công bằng mắt, dẫn đến nhiều lỗi chỉ được phát hiện khi may thử trên máy thật làm gãy kim hoặc hư hỏng vải.", bold_prefix="Thiếu kiểm soát chất lượng tự động:")
    add_bullet_item(doc, " Chỉ cho phép chọn các model máy Brother tiêu chuẩn cố định. Không hỗ trợ tùy biến vùng may hay cấu hình các tính năng đặc thù cho máy cải tiến.", bold_prefix="Không thể tùy biến thiết bị:")
    
    add_figure(doc, "final_screenshots/01_comparison_ps300b_legacy.png", 
               "Hình 2: Giao diện thế hệ cũ Brother PS-300B với hệ thống thanh công cụ rải rác và menu phức tạp", width=Inches(5.6))
    
    add_figure(doc, "final_screenshots/02_ps300c_new_ui_overview.png", 
               "Hình 3: Giao diện phẳng hiện đại hoàn toàn mới của Brother PS-300C với bố cục phân vùng khoa học", width=Inches(5.6))
    
    add_custom_heading(doc, "2.2 Bảng đối chiếu ma trận kỹ thuật 10 tiêu chí (PS-300B vs PS-300C)", level=2)
    
    comparison_data = [
        ("1. Phong cách thiết kế giao diện", "Kiểu cũ Windows XP, biểu tượng xám, nhiều menu con lồng nhau", "Giao diện phẳng hiện đại, tương phản cao, tối ưu công thái học"),
        ("2. Tìm kiếm công cụ thao tác", "Khó khăn, mất thời gian tìm nút trên thanh công cụ rải rác", "Thanh công cụ vẽ nổi (Floating Dock) thông minh, truy cập tức thì"),
        ("3. Thao tác điều hướng bản vẽ", "Chủ yếu dùng thanh cuộn thủ công, dễ giật lag", "Tích hợp công cụ Bắt điểm (Snap) & Bàn tay dịch chuyển (Pan) mượt mà"),
        ("4. Quản lý phân đoạn đường may", "Hộp thoại riêng biệt, phải bật/tắt cửa sổ phụ", "Cây danh mục Outline List luôn hiển thị thường trực kèm ảnh thumbnail"),
        ("5. Bảng tọa độ mũi kim (Point List)", "Hiển thị thô, khó tra cứu bước may (Pitch)", "Hiển thị trực quan X, Y, Pitch; chọn trên bảng sẽ sáng trên bản vẽ"),
        ("6. Nhập bản vẽ CAD định dạng DXF", "Nhập toàn bộ tệp, không xem trước, không lọc Layer", "Hộp thoại xem trước trực quan, tùy chọn từng Layer, gán Guide Data"),
        ("7. Chức năng can vẽ đường rập", "Không có hoặc thao tác phức tạp", "Hỗ trợ biến DXF thành đường tham chiếu Guide Data (màu xanh lá)"),
        ("8. Kiểm tra phát hiện lỗi (QA)", "Phụ thuộc 100% mắt thường của thợ rập", "Tự động phát hiện 5 tiêu chuẩn lỗi, làm sáng đỏ mũi vi phạm tức thì"),
        ("9. Mô phỏng động học may", "Xem mô phỏng đơn giản, không phản ánh tốc độ thực", "Mô phỏng tốc độ may, tốc độ đẩy bàn kẹp, tính Estimated Sewing Time"),
        ("10. Khả năng tùy biến máy may", "Chỉ chọn được các model máy cố định có sẵn", "Thẻ Custom Machine: tự do đặt tên, nhập khổ X/Y, bật tính năng nâng cao")
    ]
    
    tbl_comp = doc.add_table(rows=len(comparison_data) + 1, cols=3)
    tbl_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_comp)
    
    # Headers
    hc0, hc1, hc2 = tbl_comp.rows[0].cells[0], tbl_comp.rows[0].cells[1], tbl_comp.rows[0].cells[2]
    hc0.width, hc1.width, hc2.width = Inches(1.8), Inches(2.3), Inches(2.37)
    for c, t in zip([hc0, hc1, hc2], ["TIÊU CHÍ SO SÁNH", "THẾ HỆ CŨ (PS-300B)", "THẾ HỆ MỚI (PS-300C)"]):
        set_cell_background(c, HEX_PRIMARY)
        set_cell_margins(c, top=120, bottom=120, left=140, right=140)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(t)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    for r_idx, (crit, old_v, new_v) in enumerate(comparison_data, start=1):
        row = tbl_comp.rows[r_idx]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width, c1.width, c2.width = Inches(1.8), Inches(2.3), Inches(2.37)
        bg = HEX_LIGHT_BLUE if r_idx % 2 == 1 else "FFFFFF"
        for c in [c0, c1, c2]:
            set_cell_background(c, bg)
            set_cell_margins(c, top=90, bottom=90, left=120, right=120)
            
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(crit)
        r0.bold = True
        r0.font.name = "Arial"
        r0.font.size = Pt(8.5)
        r0.font.color.rgb = COLOR_SECONDARY
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(old_v)
        r1.font.name = "Arial"
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = COLOR_MUTED
        
        p2 = c2.paragraphs[0]
        p2.paragraph_format.space_after = Pt(0)
        r2 = p2.add_run(new_v)
        r2.bold = True
        r2.font.name = "Arial"
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = COLOR_PRIMARY

    doc.add_page_break()

    # ----------------------------------------------------
    # CHƯƠNG 3: CẤU TRÚC GIAO DIỆN NGƯỜI DÙNG MỚI
    # ----------------------------------------------------
    add_custom_heading(doc, "CHƯƠNG 3: CẤU TRÚC GIAO DIỆN NGƯỜI DÙNG MỚI (REDESIGNED UI & NAVIGATION)", level=1)
    
    add_custom_heading(doc, "3.1 Phân tích 5 khu vực làm việc cốt lõi trên PS-300C", level=2)
    add_body_p(doc, 
               "Giao diện của Brother PS-300C được xây dựng trên triết lý tối giản và tập trung vào luồng công việc (Workflow-centric design). Toàn bộ màn hình được chia thành 5 khu vực làm việc khoa học:")
    
    add_bullet_item(doc, " Chứa menu chính (File, Edit, View, Tools, Help), hệ số phóng đại (Zoom %), các chế độ hiển thị (Outline, Punch Point, Needle Point), chọn model máy may hiện hành (ví dụ BAS365K), nút nhập chú thích (Enter comment) và nút chuyển sang chế độ mô phỏng (Preview).", bold_prefix="1. Thanh điều khiển trên cùng (Top Ribbon / Control Bar):")
    add_bullet_item(doc, " Luôn hiển thị thường trực ở cạnh trái, giúp quản lý toàn bộ các phân đoạn may mà không cần mở các cửa sổ phụ. Mỗi phân đoạn hiển thị số thứ tự, hình thu nhỏ đường may và số lượng mũi may cụ thể.", bold_prefix="2. Danh mục đường may thường trực (Left Outline List):")
    add_bullet_item(doc, " Vùng làm việc đồ họa độ nét cao với lưới tọa độ (Grid), hiển thị đường may thực tế, đường chỉ nhảy (Jump stitch - nét đứt màu xanh dương), điểm dừng cắt chỉ (biểu tượng kéo màu xanh lá) và đường chuẩn DXF.", bold_prefix="3. Không gian bản vẽ trung tâm (Central Canvas):")
    add_bullet_item(doc, " Nằm gọn gàng ở cạnh dưới màn hình, tích hợp đầy đủ công cụ chọn lựa, bàn tay di chuyển (Pan), vẽ đoạn thẳng, đường cong Spline, hình hộp, hình tròn, elip, cung tròn, góc nhọn và thước đo.", bold_prefix="4. Thanh công cụ vẽ nổi (Floating Tool Dock):")
    add_bullet_item(doc, " Cạnh phải hiển thị thông tin chung (General Info: số outline, số mũi may) và tham số đầu vào (Input parameter). Thanh đáy hiển thị tên tệp, chế độ may (Detail/Medium/Overview), tọa độ chuột (X, Y mm) và huy hiệu cảnh báo lỗi thời gian thực.", bold_prefix="5. Bảng thuộc tính bên phải & Thanh trạng thái dưới cùng:")
    
    add_figure(doc, "final_screenshots/03_snap_and_pan_navigation.png", 
               "Hình 4: Công cụ Bắt điểm (Snap) và Cuộn di chuyển (Pan) hỗ trợ biên tập mượt mà", width=Inches(5.8))
    
    add_custom_heading(doc, "3.2 Cơ chế Bắt điểm (Snap) và Điều hướng (Pan) thông minh", level=2)
    add_body_p(doc, 
               "Trong phiên bản PS-300C, Brother đã nâng cấp cơ chế điều hướng bản vẽ lên tầm cao mới, tương đương với các phần mềm CAD chuyên nghiệp hàng đầu:")
    
    add_bullet_item(doc, " Khi vẽ hoặc dịch chuyển các điểm may, con trỏ chuột sẽ tự động bắt dính chính xác vào các điểm nút (Endpoints), giao điểm hoặc điểm lưới gần nhất, đảm bảo tính liên tục của đường may.", bold_prefix="Tính năng Tự động Bắt điểm (Snap):")
    add_bullet_item(doc, " Trong các trường hợp cần di chuyển điểm may tự do mà không muốn bị hút vào điểm nút, người dùng chỉ cần nhấn giữ phím Ctrl trên bàn phím. Thao tác này giúp tinh chỉnh những đường cong vi mô vô cùng chính xác.", bold_prefix="Phím tắt tạm tắt Snap (Hold Ctrl):")
    add_bullet_item(doc, " Người dùng có thể nhấp chọn biểu tượng Bàn tay trên thanh Floating Dock hoặc nhấn phím cuộn chuột (Middle Mouse Click) để kéo rê không gian làm việc mượt mà mà không làm thay đổi tỷ lệ hay lệch tọa độ.", bold_prefix="Công cụ Pan (Dịch chuyển khung nhìn):")

    add_callout(doc, 
                "Người dùng có thể phóng to nhanh bằng cách nhấn giữ phím Ctrl + Lăn chuột (Ctrl + Wheel) hoặc nhấn phím Home để tự động đưa toàn bộ đường may vừa vặn vào khung nhìn (Fit to sewing area).",
                title="MẸO NĂNG SUẤT (PRO TIP)", box_type="tip")
                
    # ----------------------------------------------------
    # CHƯƠNG 4: QUY TRÌNH BIÊN TẬP VÀ QUẢN LÝ DỮ LIỆU ĐƯỜNG MAY
    # ----------------------------------------------------
    add_custom_heading(doc, "CHƯƠNG 4: QUY TRÌNH BIÊN TẬP VÀ QUẢN LÝ DỮ LIỆU ĐƯỜNG MAY (STREAMLINED WORKFLOWS)", level=1)
    
    add_custom_heading(doc, "4.1 Quản lý danh mục đường may đa tầng (Outline List Management)", level=2)
    add_body_p(doc, 
               "Đối với các sản phẩm may phức tạp (như may giày thể thao, túi xách cao cấp hoặc ghế ôtô), một chương trình may có thể chứa từ 20 đến hơn 100 phân đoạn may khác nhau. Trong PS-300C, thanh Outline List thường trực bên trái giúp kiểm soát hoàn hảo cấu trúc này:")
    
    add_bullet_item(doc, " Mỗi phần tử trong danh sách thể hiện trực tiếp hình dáng đường may thu nhỏ và tổng số mũi may (ví dụ: Outline 118: 30 stitches, Outline 119: 37 stitches).", bold_prefix="Xem trước hình thu nhỏ (Thumbnail):")
    add_bullet_item(doc, " Nhấp chuột vào bất kỳ phân đoạn nào trên danh sách sẽ tự động kích hoạt và làm sáng phân đoạn đó trên màn hình đồ họa, giúp kỹ thuật viên không bị nhầm lẫn.", bold_prefix="Lựa chọn tức thì:")
    add_bullet_item(doc, " Người dùng có thể kéo thả để hoán đổi thứ tự may giữa các phân đoạn hoặc xóa, ẩn/hiện từng đường may theo nhu cầu sản xuất.", bold_prefix="Sắp xếp linh hoạt:")
    
    add_figure(doc, "final_screenshots/04_outline_list_management.png", 
               "Hình 5: Danh mục đường may thường trực Outline List bên trái không gian làm việc với hình thu nhỏ và số mũi may", width=Inches(5.8))
    
    add_custom_heading(doc, "4.2 Kiểm soát tọa độ mũi kim và bước may (Point List & Stitch Pitch)", level=2)
    add_body_p(doc, 
               "Khi chuyển sang chế độ xem mũi kim chi tiết (Needle Point Mode), bảng danh sách mũi kim (Point List) sẽ mở rộng dưới từng phân đoạn Outline, mang lại khả năng kiểm soát dữ liệu ở mức độ vi mô:")
    
    add_bullet_item(doc, " Bảng hiển thị 3 cột dữ liệu cốt lõi cho từng mũi may: Số thứ tự mũi, Tọa độ trục X (mm), Tọa độ trục Y (mm) và Bước may (Pitch - khoảng cách giữa 2 mũi kim liên tiếp).", bold_prefix="Bảng dữ liệu 3 cột chuẩn xác:")
    add_bullet_item(doc, " Khi chọn một hàng trên bảng dữ liệu, điểm may tương ứng trên màn hình sẽ chuyển sang màu đỏ rực rỡ và ngược lại. Tính năng này giúp kỹ thuật viên dễ dàng tìm thấy mũi may bị lỗi bước mũi để điều chỉnh.", bold_prefix="Đồng bộ hóa trực quan hai chiều:")
    add_bullet_item(doc, " Bảng dữ liệu hỗ trợ phân trang thông minh (ví dụ: trang < 4/4 >), giúp tải dữ liệu cực nhanh ngay cả khi chương trình có hàng chục nghìn mũi kim.", bold_prefix="Phân trang tối ưu hiệu năng:")
    
    add_figure(doc, "final_screenshots/point_list_68s.png", 
               "Hình 6: Bảng tọa độ mũi kim Point List hiển thị chi tiết X, Y và Stitch Pitch đồng bộ trực tiếp với màn hình may", width=Inches(5.8))
    
    add_custom_heading(doc, "4.3 Bảng thuộc tính nâng cao và Cài đặt lại mũi (Needle Point Info & Back Tack)", level=2)
    add_body_p(doc, 
               "Ở bảng thuộc tính cạnh phải (Needle Point Info), kỹ thuật viên có thể can thiệp sâu vào các thông số công nghệ của từng điểm may:")
    
    add_bullet_item(doc, " Cho phép tinh chỉnh chính xác vị trí mũi may bằng cách gõ trực tiếp số đo tọa độ X và Y (mm) thay vì phải kéo chuột.", bold_prefix="Căn chỉnh tọa độ Placement (X, Y mm):")
    add_bullet_item(doc, " Thay đổi trạng thái mũi kim giữa Stitch (mũi may thường), Jump (mũi nhảy chỉ) hoặc chèn lệnh cắt chỉ tự động.", bold_prefix="Thuộc tính mũi kim (Needle points attribute):")
    add_bullet_item(doc, " Cung cấp công cụ thiết lập mũi may gia cố tự động ở đầu hoặc cuối đường may: Number of Back Tack Iterations (Số chu kỳ lặp lại mũi, ví dụ: 2) và Number of Back Tack Stitches (Số lượng mũi may lại bọ, ví dụ: 2 mũi). Nhấp nút Apply để áp dụng tức thì.", bold_prefix="Cấu hình lại mũi / Lại bọ (Back Tack):")
    add_bullet_item(doc, " Cho phép chèn các mã lệnh điều khiển phần cứng của máy may như: mã thay đổi lực căng chỉ kỹ thuật số, mã nâng hạ chân vịt tự động, mã cảm biến độ dày vật liệu.", bold_prefix="Chèn mã chức năng phụ trợ (Codes):")
    
    add_figure(doc, "final_screenshots/shortcuts_74s.png", 
               "Hình 7: Bảng thuộc tính Needle Point Info, cấu hình lại mũi Back Tack và danh mục mã lệnh máy may Codes", width=Inches(5.8))

    doc.add_page_break()

    # ----------------------------------------------------
    # CHƯƠNG 5: BẢNG TRA CỨU PHÍM TẮT TOÀN DIỆN
    # ----------------------------------------------------
    add_custom_heading(doc, "CHƯƠNG 5: BẢNG TRA CỨU PHÍM TẮT TOÀN DIỆN (KEYBOARD SHORTCUTS CHEAT SHEET)", level=1)
    
    add_body_p(doc, 
               "Để tối đa hóa tốc độ thao tác và đạt hiệu suất cao nhất trong môi trường công nghiệp, Brother PS-300C trang bị hệ thống phím tắt toàn diện được phân chia thành 4 nhóm nghiệp vụ chính (Edit, File, View, Selection).")
    
    add_figure(doc, "final_screenshots/shortcuts_modal_76s.png", 
               "Hình 8: Cửa sổ tra cứu phím tắt Keyboard Shortcuts chính thức trên phần mềm Brother PS-300C", width=Inches(5.8))
    
    shortcuts_data = [
        # Edit
        ("Ctrl + C", "Sao chép đối tượng hoặc phân đoạn đường may đã chọn", "Biên tập (Edit)"),
        ("Ctrl + X", "Cắt đối tượng hoặc phân đoạn đường may", "Biên tập (Edit)"),
        ("Ctrl + V", "Dán đối tượng vào vị trí con trỏ", "Biên tập (Edit)"),
        ("Ctrl + Z", "Hoàn tác thao tác trước đó (Undo)", "Biên tập (Edit)"),
        ("Ctrl + Y", "Làm lại thao tác vừa hủy (Redo)", "Biên tập (Edit)"),
        ("Del (Delete)", "Xóa đối tượng hoặc điểm may đang chọn", "Biên tập (Edit)"),
        ("Ctrl + R / F5", "Làm mới lại dữ liệu hiển thị (Refresh)", "Biên tập (Edit)"),
        ("Ctrl + Phím mũi tên", "Sao chép nhanh đường bao (Copy outline)", "Biên tập (Edit)"),
        ("Enter", "Xác nhận nhập liệu (Confirm input)", "Biên tập (Edit)"),
        ("Esc", "Hủy bỏ thao tác nhập liệu hiện tại (Cancel input)", "Biên tập (Edit)"),
        ("Ctrl + I", "Mở hộp thoại nhập kích thước số (Open Numeric Input Dialog)", "Biên tập (Edit)"),
        ("W / A / S / D", "Dịch chuyển điểm may sang Lên / Trái / Xuống / Phải (bước nhỏ)", "Biên tập (Edit)"),
        ("Shift + W / A / S / D", "Dịch chuyển điểm may sang Lên / Trái / Xuống / Phải (bước lớn)", "Biên tập (Edit)"),
        
        # File
        ("Ctrl + N", "Tạo tệp may mới (New File)", "Tệp tin (File)"),
        ("Ctrl + O", "Mở tệp dữ liệu có sẵn (.emb, .sew, .dxf) (Open File)", "Tệp tin (File)"),
        ("Ctrl + S", "Lưu tệp may hiện tại (Save File)", "Tệp tin (File)"),
        ("Ctrl + Q", "Thoát khỏi ứng dụng PS-300C (Exit App)", "Tệp tin (File)"),
        
        # View
        ("Ctrl + Con lăn chuột", "Thu phóng to / nhỏ bản vẽ (Zoom in / out)", "Khung nhìn (View)"),
        ("Con lăn chuột (Wheel)", "Cuộn khung nhìn lên / xuống (Scroll up / down)", "Khung nhìn (View)"),
        ("Shift + Con lăn chuột", "Cuộn khung nhìn sang trái / phải (Scroll left / right)", "Khung nhìn (View)"),
        ("Ctrl + / Ctrl -", "Phóng to / Thu nhỏ tỷ lệ cố định (Zoom in / out)", "Khung nhìn (View)"),
        ("Home", "Tự động thu phóng vừa vặn vùng may (Fit to sewing area)", "Khung nhìn (View)"),
        
        # Selection
        ("Ctrl + A", "Chọn tất cả đối tượng trên bản vẽ (Select All)", "Lựa chọn (Selection)"),
        ("Phím Mũi tên Lên / Phải", "Chọn đối tượng kế tiếp (Select next object)", "Lựa chọn (Selection)"),
        ("Phím Mũi tên Xuống / Trái", "Chọn đối tượng liền trước (Select previous object)", "Lựa chọn (Selection)"),
        ("Shift + Phím Mũi tên", "Mở rộng vùng lựa chọn (Expand selection)", "Lựa chọn (Selection)"),
        ("Space (Phím cách)", "Bật / tắt chọn đối tượng đang tiêu điểm (Toggle selection)", "Lựa chọn (Selection)"),
        ("Ctrl (Nhấn giữ)", "Tạm thời vô hiệu hóa bắt điểm tự động (Disable snap)", "Lựa chọn (Selection)"),
        ("Alt (Nhấn giữ)", "Tạm thời khóa chọn và di chuyển đối tượng", "Lựa chọn (Selection)"),
        ("Ctrl + Nhấp chuột", "Chọn đồng thời nhiều đối tượng riêng lẻ (Multiple Selection)", "Lựa chọn (Selection)"),
        ("Ctrl + F", "Mở công cụ tìm kiếm đối tượng / phân đoạn (Find)", "Lựa chọn (Selection)")
    ]
    
    tbl_sc = doc.add_table(rows=len(shortcuts_data) + 1, cols=3)
    tbl_sc.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_sc)
    
    # Header
    for c, title, w in zip(tbl_sc.rows[0].cells, ["PHÍM TẮT", "CHỨC NĂNG NGHIỆP VỤ", "NHÓM CHỨC NĂNG"], [Inches(1.8), Inches(3.3), Inches(1.37)]):
        c.width = w
        set_cell_background(c, HEX_PRIMARY)
        set_cell_margins(c, top=100, bottom=100, left=120, right=120)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(title)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    for r_idx, (keys, f_desc, f_grp) in enumerate(shortcuts_data, start=1):
        row = tbl_sc.rows[r_idx]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width, c1.width, c2.width = Inches(1.8), Inches(3.3), Inches(1.37)
        bg = HEX_LIGHT_BLUE if r_idx % 2 == 1 else "FFFFFF"
        for c in [c0, c1, c2]:
            set_cell_background(c, bg)
            set_cell_margins(c, top=70, bottom=70, left=100, right=100)
            
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(keys)
        r0.bold = True
        r0.font.name = "Arial"
        r0.font.size = Pt(8.5)
        r0.font.color.rgb = COLOR_PRIMARY
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(f_desc)
        r1.font.name = "Arial"
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = COLOR_TEXT
        
        p2 = c2.paragraphs[0]
        p2.paragraph_format.space_after = Pt(0)
        r2 = p2.add_run(f_grp)
        r2.font.name = "Arial"
        r2.font.size = Pt(8)
        r2.font.color.rgb = COLOR_MUTED

    doc.add_page_break()

    # ----------------------------------------------------
    # CHƯƠNG 6: TÍCH HỢP VÀ BÓC TÁCH BẢN VẼ CAD ĐỊNH DẠNG DXF
    # ----------------------------------------------------
    add_custom_heading(doc, "CHƯƠNG 6: TÍCH HỢP VÀ BÓC TÁCH BẢN VẼ CAD ĐỊNH DẠNG DXF (ENHANCED DXF INTEGRATION)", level=1)
    
    add_custom_heading(doc, "6.1 Khả năng tương thích tệp CAD mở rộng và Cửa sổ DXF Import", level=2)
    add_body_p(doc, 
               "Tích hợp dữ liệu từ phần mềm thiết kế rập CAD 2D/3D là công đoạn sống còn trong quy trình sản xuất hiện đại. Brother PS-300C hỗ trợ mở trực tiếp nhiều định dạng tệp bao gồm: Tệp mẫu thêu/may Brother (*.emb, *.sew) và tệp bản vẽ CAD tiêu chuẩn công nghiệp (*.dxf) từ AutoCAD, Optitex, Lectra, Gerber, Shoemaster, Romans CAD.")
    
    add_figure(doc, "final_screenshots/07_dxf_file_open_dialog.png", 
               "Hình 9: Hộp thoại mở tệp hỗ trợ định dạng DXF, EMB, SEW", width=Inches(5.6))
    
    add_body_p(doc, 
               "Khi chọn tệp DXF (ví dụ Draw2 1.DXF), thay vì nạp ngay lập tức như phiên bản cũ, PS-300C hiển thị một cửa sổ bóc tách chuyên nghiệp mang tên DXF Import với hai bảng chức năng:")
    
    add_bullet_item(doc, " Màn hình bên trái hiển thị toàn bộ các đường nét hình học trong tệp CAD với màu xanh lá trực quan, cho phép người dùng thu phóng và kiểm tra kỹ trước khi đưa vào không gian may.", bold_prefix="1. Khung xem trước bản vẽ CAD (Preview Pane):")
    add_bullet_item(doc, " Danh sách liệt kê tất cả các Layer có trong tệp CAD (ví dụ: Layer S-1, Layer S-3) kèm theo hình thu nhỏ của từng Layer. Người dùng có thể chọn hoặc bỏ chọn từng Layer bằng các nút '+ Select all' và '- Deselect all'.", bold_prefix="2. Bảng chọn lựa Layer (Select Layer):")
    
    add_figure(doc, "final_screenshots/dxf_86s.png", 
               "Hình 10: Cửa sổ DXF Import xem trước bản vẽ CAD và chọn lọc từng Layer độc lập", width=Inches(5.8))
    
    add_custom_heading(doc, "6.2 Phân định vai trò Layer: Sewing Data vs Guide Data", level=2)
    add_body_p(doc, 
               "Điểm cải tiến mang tính cách mạng nhất của PS-300C trong tích hợp DXF chính là cho phép người dùng ấn định vai trò công nghệ cho từng Layer nhập vào:")
    
    add_bullet_item(doc, " Layer được chọn sẽ chuyển đổi trực tiếp thành các mũi may và đường may thực tế để máy may thực hiện.", bold_prefix="Sewing Data (Dữ liệu may):")
    add_bullet_item(doc, " Layer được chọn sẽ được nhập vào như một 'đường dẫn tham chiếu' (Reference Guide) hiển thị dưới dạng đường nét mảnh màu xanh lá cây trên bản vẽ. Dữ liệu này KHÔNG tạo ra mũi may thực tế trên máy mà đóng vai trò như bản vẽ rập nền chuẩn xác.", bold_prefix="Guide Data (Dữ liệu rập nền tham chiếu):")
    
    add_custom_heading(doc, "6.3 Cấu hình tham số nhập CAD (DXF Import Settings)", level=2)
    add_body_p(doc, 
               "Tại thẻ Import Settings, PS-300C cung cấp bộ công cụ chuẩn hóa hình học mạnh mẽ:")
    
    add_bullet_item(doc, " Tùy chọn mm hoặc inch để đảm bảo tỷ lệ bản vẽ rập hoàn toàn trùng khớp 1:1 với kích thước thực tế.", bold_prefix="Đơn vị đo lường (Unit):")
    add_bullet_item(doc, " Tự động đưa trọng tâm bản vẽ CAD về chính giữa tâm gốc tọa độ (X=0, Y=0) của bàn kẹp máy may.", bold_prefix="Căn giữa tự động (Move to center):")
    add_bullet_item(doc, " Cho phép phóng to hoặc thu nhỏ tỷ lệ kích thước bản vẽ (mặc định 1.0).", bold_prefix="Tỷ lệ co giãn (Scale):")
    add_bullet_item(doc, " Tự động phát hiện và loại bỏ các đường bao rác hoặc nét vẽ thừa có kích thước nhỏ hơn ngưỡng quy định (ví dụ ngưỡng 1.0 mm), giúp bản vẽ sạch sẽ và không gây nghẽn dữ liệu.", bold_prefix="Lọc đường bao rác (Remove small outlines):")
    
    add_figure(doc, "final_screenshots/dxf_imported_98s.png", 
               "Hình 11: Cấu hình tham số nhập khẩu bản vẽ CAD (DXF Import Settings)", width=Inches(5.6))
    
    add_custom_heading(doc, "6.4 Ứng dụng Guide Data và Tối ưu hóa thứ tự may (Sequence Optimization)", level=2)
    add_body_p(doc, 
               "Sau khi nhập, bản vẽ CAD đóng vai trò như một khuôn mẫu nền tham chiếu cực kỳ chuẩn xác:")
    add_body_p(doc, 
               "Kỹ thuật viên có thể can vẽ các đường may mới bám sát theo đường rập CAD hoặc sử dụng các công cụ chỉnh sửa để nắn chỉnh đường may ăn khớp hoàn hảo với biên dạng khuôn gá sản xuất. Bên cạnh đó, thanh Sequence bên trái cung cấp nút chức năng 'Optimize Sequence' (Tối ưu hóa thứ tự may), tự động sắp xếp lại trình tự các đường may sao cho tổng quãng đường di chuyển của kim là ngắn nhất, giảm thiểu tối đa các đường chỉ nhảy (Jump stitch).")
    
    add_figure(doc, "final_screenshots/dxf_done_103s.png", 
               "Hình 12: Bản vẽ DXF làm đường dẫn tham chiếu Guide Data (màu xanh lá) kết hợp bố trí đường may và Sequence", width=Inches(5.8))

    doc.add_page_break()

    # ----------------------------------------------------
    # CHƯƠNG 7: HỆ THỐNG KIỂM SOÁT CHẤT LƯỢNG VÀ PHÁT HIỆN LỖI
    # ----------------------------------------------------
    add_custom_heading(doc, "CHƯƠNG 7: HỆ THỐNG KIỂM SOÁT CHẤT LƯỢNG VÀ PHÁT HIỆN LỖI TỰ ĐỘNG (QUALITY VERIFICATION & ALERTS)", level=1)
    
    add_custom_heading(doc, "7.1 Cơ chế cảnh báo lỗi thời gian thực (Real-time Abnormal Settings Detection)", level=2)
    add_body_p(doc, 
               "Tạo dữ liệu nhanh là cần thiết, nhưng tạo dữ liệu CHÍNH XÁC còn quan trọng hơn rất nhiều. Một mũi may bị lỗi bước mũi hoặc nằm ngoài phạm vi may có thể dẫn đến hậu quả nghiêm trọng: gãy kim, đứt chỉ, rách lớp da thành phẩm đắt tiền hoặc làm cong vênh bàn kẹp.")
    
    add_body_p(doc, 
               "Brother PS-300C tích hợp cơ chế bảo vệ chất lượng tự động hoạt động liên tục trong thời gian thực:")
    add_bullet_item(doc, " Ở góc dưới bên phải thanh trạng thái luôn hiển thị một biểu tượng chấm than màu đỏ kèm số lượng lỗi phát hiện (ví dụ: ! 7).", bold_prefix="Huy hiệu đếm lỗi (Warning Counter Badge):")
    add_bullet_item(doc, " Nhấp vào huy hiệu sẽ mở ra bảng danh sách Warnings liệt kê chi tiết từng vi phạm (ví dụ: #1 Pitch is too small., #2 Pitch is too small., ...).", bold_prefix="Bảng liệt kê lỗi chi tiết (Warnings Panel):")
    
    add_figure(doc, "final_screenshots/11_abnormal_setting_detection_warnings.png", 
               "Hình 13: Bảng cảnh báo Warnings tự động phát hiện các lỗi cài đặt bất thường (Pitch is too small)", width=Inches(5.8))
    
    add_custom_heading(doc, "7.2 Cơ chế định vị lỗi trực quan tương tác (Interactive Error Locating)", level=2)
    add_body_p(doc, 
               "Điểm độc đáo hàng đầu của PS-300C là khả năng điều hướng lỗi cực kỳ thông minh:")
    add_body_p(doc, 
               "Khi người dùng nhấp chuột vào bất kỳ dòng thông báo lỗi nào trong danh sách Warnings (ví dụ nhấp vào '#6 Pitch is too small.'), phần mềm lập tức tự động thu phóng (Zoom-in) vùng bản vẽ đó và làm sáng mũi may vi phạm bằng MÀU ĐỎ RỰC RỠ, nổi bật hoàn toàn giữa các mũi may màu xanh dương bình thường. Kỹ thuật viên có thể ngay lập tức sửa lỗi mà không cần phải lùng sục tọa độ trên hàng nghìn mũi kim.")
    
    add_figure(doc, "final_screenshots/12_interactive_error_highlight_red.png", 
               "Hình 14: Nhấp chọn dòng cảnh báo lỗi để phần mềm tự động zoom và làm sáng đỏ vị trí mũi may vi phạm", width=Inches(5.8))
    
    add_custom_heading(doc, "7.3 Cấu hình tùy biến 5 tiêu chuẩn kiểm soát chất lượng (Customizable Alerts)", level=2)
    add_body_p(doc, 
               "Mỗi nhà máy, mỗi loại vật liệu may (vải thun, denim dày, da thật, vải túi khí ôtô) đều có những yêu cầu kỹ thuật riêng biệt. Nhấp vào biểu tượng bộ lọc trên bảng Warnings sẽ mở ra hộp thoại cấu hình 5 tiêu chuẩn phát hiện lỗi tùy biến:")
    
    alert_rules = [
        ("1. Short Pitch Detection", "Bật/Tắt (Toggle ON/OFF) & Cài đặt ngưỡng mm (ví dụ: 2.0 mm)", "Phát hiện các mũi may có bước mũi quá ngắn (nhỏ hơn ngưỡng quy định). Giúp ngăn ngừa hiện tượng kim đâm liên tục vào một điểm làm nát vải, rách da hoặc đứt chỉ."),
        ("2. Nearby Punch Points Detection", "Bật/Tắt & Cài đặt ngưỡng mm (ví dụ: 2.0 mm)", "Phát hiện các điểm dập kim (Punch Points) nằm quá gần nhau, tránh việc dao đục lỗ hay kim dập làm hỏng kết cấu rập."),
        ("3. Deviated Pitch Detection", "Bật/Tắt & Cài đặt ngưỡng % (ví dụ: 10%)", "Phát hiện sự thay đổi bước mũi đột ngột lệch quá tỷ lệ phần trăm cho phép so với bước mũi danh định, đảm bảo tính thẩm mỹ và độ bền đồng đều của đường may."),
        ("4. Empty Outline Detection", "Bật/Tắt (Toggle ON/OFF)", "Phát hiện các đường bao rỗng không chứa mũi may nào, cảnh báo kỹ thuật viên xóa bỏ hoặc bổ sung mũi may."),
        ("5. Out of Sewing Area Detection", "Bật/Tắt (Toggle ON/OFF)", "Tự động so sánh tọa độ tất cả các mũi may với giới hạn khổ may vật lý của máy đã chọn. Ngăn chặn tuyệt đối việc kim may đâm vào khung kẹp kim loại gây gãy kim, gãy ổ chao.")
    ]
    
    tbl_ar = doc.add_table(rows=len(alert_rules) + 1, cols=3)
    tbl_ar.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_ar)
    
    for c, title, w in zip(tbl_ar.rows[0].cells, ["TIÊU CHUẨN KIỂM TRA", "CÀI ĐẶT NGƯỠNG", "Ý NGHĨA KỸ THUẬT & AN TOÀN SẢN XUẤT"], [Inches(1.8), Inches(1.8), Inches(2.87)]):
        c.width = w
        set_cell_background(c, HEX_PRIMARY)
        set_cell_margins(c, top=100, bottom=100, left=120, right=120)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(title)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    for r_idx, (t_name, t_set, t_mean) in enumerate(alert_rules, start=1):
        row = tbl_ar.rows[r_idx]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width, c1.width, c2.width = Inches(1.8), Inches(1.8), Inches(2.87)
        bg = HEX_LIGHT_BLUE if r_idx % 2 == 1 else "FFFFFF"
        for c in [c0, c1, c2]:
            set_cell_background(c, bg)
            set_cell_margins(c, top=80, bottom=80, left=100, right=100)
            
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(t_name)
        r0.bold = True
        r0.font.name = "Arial"
        r0.font.size = Pt(8.5)
        r0.font.color.rgb = COLOR_SECONDARY
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(t_set)
        r1.bold = True
        r1.font.name = "Arial"
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = COLOR_PRIMARY
        
        p2 = c2.paragraphs[0]
        p2.paragraph_format.space_after = Pt(0)
        r2 = p2.add_run(t_mean)
        r2.font.name = "Arial"
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = COLOR_TEXT
        
    add_figure(doc, "final_screenshots/alerts_config_121s.png", 
               "Hình 15: Hộp thoại cấu hình 5 tiêu chuẩn phát hiện lỗi và cảnh báo bất thường tùy biến", width=Inches(5.6))

    doc.add_page_break()

    # ----------------------------------------------------
    # CHƯƠNG 8: MÔ PHỎNG ĐƯỜNG MAY & DỰ TOÁN THỜI GIAN CHU KỲ
    # ----------------------------------------------------
    add_custom_heading(doc, "CHƯƠNG 8: MÔ PHỎNG ĐƯỜNG MAY VÀ DỰ TOÁN THỜI GIAN CHU KỲ (PLAYBACK SIMULATION & CYCLE TIME)", level=1)
    
    add_custom_heading(doc, "8.1 Chế độ mô phỏng động học thực tế (Enhanced Playback Function)", level=2)
    add_body_p(doc, 
               "Trước khi gửi tệp dữ liệu may xuống xưởng, việc xem trước chuyển động thực tế là yêu cầu bắt buộc để kiểm tra an toàn va chạm. Nhấp vào nút 'Preview' trên thanh điều khiển sẽ đưa phần mềm vào chế độ mô phỏng động học:")
    
    add_bullet_item(doc, " Hiển thị chuyển động di chuyển mũi may từng bước theo đúng tốc độ thực tế của đầu máy may Brother.", bold_prefix="Mô phỏng chuyển động kim thực tế:")
    add_bullet_item(doc, " Ở cạnh dưới màn hình tích hợp thanh trượt tiến trình cho phép tua nhanh, tạm dừng, lùi từng mũi hoặc nhảy tới vị trí bất kỳ kèm bộ đếm vị trí mũi may chính xác (ví dụ: mũi 014 / 854 mũi).", bold_prefix="Thanh điều khiển tiến trình may (Timeline Scrubber):")
    add_bullet_item(doc, " Cho phép chạy mô phỏng ở nhiều tốc độ (x0.5, x1.0, x2.0, x4.0) để quan sát kỹ những đoạn cua ngặt khó may.", bold_prefix="Hệ số tốc độ mô phỏng:")
    
    add_figure(doc, "final_screenshots/13_playback_simulation_controls.png", 
               "Hình 16: Bảng điều khiển mô phỏng may Playback Simulation và các tham số động học", width=Inches(5.8))
    
    add_custom_heading(doc, "8.2 Ba tham số động học vận hành của thiết bị may", level=2)
    add_body_p(doc, 
               "Tại bảng điều khiển Sewing Time bên phải, người dùng có thể nhập các thông số kỹ thuật thực tế của dây chuyền sản xuất:")
    
    add_bullet_item(doc, " Tốc độ quay của trục chính máy may, tính bằng mũi may trên phút (ví dụ: 1,500 sti/min hoặc lên tới 2,800 sti/min).", bold_prefix="1. Sewing Speed (sti/min):")
    add_bullet_item(doc, " Vận tốc dịch chuyển của bàn kẹp X-Y giữa các mũi may hoặc trong những đoạn nhảy chỉ (Jump stitch), tính bằng mm/giây (ví dụ: 200 mm/s hoặc 300 mm/s).", bold_prefix="2. Feed Speed (mm/s):")
    add_bullet_item(doc, " Thời gian máy dừng lại để thực hiện chu kỳ cắt chỉ và gạt chỉ tự động, tính bằng giây (ví dụ: 0.3s hoặc 0.5s).", bold_prefix="3. Trim Duration (sec):")
    
    add_custom_heading(doc, "8.3 Tính toán dự toán thời gian may chính xác (Estimated Sewing Time)", level=2)
    add_body_p(doc, 
               "Dựa trên 3 thông số động học trên kết hợp với quỹ đạo thực tế của tất cả các mũi may, PS-300C tự động tính toán và hiển thị thời gian may hoàn thành sản phẩm theo định dạng phút : giây với kích thước chữ rất lớn (ví dụ: 1 : 17 hoặc 1 : 41).")
    
    add_figure(doc, "final_screenshots/14_estimated_sewing_time_display.png", 
               "Hình 17: Tính năng tính toán và hiển thị thời gian may chu kỳ Estimated Sewing Time (1:17)", width=Inches(5.8))
    
    add_figure(doc, "final_screenshots/15_playback_motion_animation.png", 
               "Hình 18: Đồ họa mô phỏng chuyển động mũi kim may và bàn kẹp theo thời gian thực (Estimated Time: 1:41)", width=Inches(5.8))
    
    add_callout(doc, 
                "Tính năng Estimated Sewing Time mang lại giá trị vô cùng to lớn cho Kỹ sư IE (Industrial Engineering): Cho phép tính toán chính xác thời gian chu kỳ (Cycle Time), định mức năng suất (UPH - Units Per Hour) và cân bằng chuyền may (Line Balancing) ngay trên máy tính mà không cần phải bấm giờ thực nghiệm tại xưởng may.",
                title="ỨNG DỤNG CHO KỸ SƯ IE & QUẢN LÝ SẢN XUẤT", box_type="ie")

    doc.add_page_break()

    # ----------------------------------------------------
    # CHƯƠNG 9: TÙY BIẾN THÔNG SỐ VÀ CẤU HÌNH THIẾT BỊ MAY THEO XƯỞNG
    # (ĐIỂM NHẤN MỐC THỜI GIAN T=146S)
    # ----------------------------------------------------
    add_custom_heading(doc, "CHƯƠNG 9: TÙY BIẾN THÔNG SỐ VÀ CẤU HÌNH THIẾT BỊ MAY THEO XƯỞNG (MACHINE CUSTOMIZATION - ĐIỂM NHẤN T=146S)", level=1)
    
    add_custom_heading(doc, "9.1 Phân tích điểm nhấn tại mốc thời gian 146 giây (2m 26s)", level=2)
    add_body_p(doc, 
               "Tại mốc thời gian 146s (2 phút 26 giây) của video, Brother giới thiệu một trong những tính năng đột phá và được mong đợi nhất của PS-300C:")
    add_body_p(doc, 
               "\"PS-300C also offers greater machine compatibility. With the machine customization feature, users can configure machine information themselves. This enables support for customized order machines, equipment modified machines, and unique production requirements. Create sewing data that truly matches your factory environment.\"")
    
    add_body_p(doc, 
               "Ý nghĩa công nghiệp thực tiễn của mốc 146s:")
    add_bullet_item(doc, " Trong các nhà máy may công nghiệp lớn, rất nhiều máy may Brother BAS được đặt hàng riêng với khổ may mở rộng hoặc cải tiến bộ phận truyền động.", bold_prefix="Máy may đặt hàng riêng (Customized Order Machines):")
    add_bullet_item(doc, " Để may các chi tiết khó (như may cổ áo, tra túi, may quai dép, may logo 3D), kỹ thuật viên nhà máy thường tự độ chế bàn kẹp (Jig/Clamp) hoặc gắn thêm cảm biến phụ trợ.", bold_prefix="Máy may cải tiến / Độ chế (Equipment Modified Machines):")
    add_bullet_item(doc, " Trước đây với PS-300B, người dùng bị giới hạn trong các thông số máy mặc định của hãng. Với PS-300C, người dùng có toàn quyền thiết lập một 'hồ sơ máy mới' hoàn toàn phù hợp với thực tế xưởng may.", bold_prefix="Tự do làm chủ thiết bị:")
    
    add_custom_heading(doc, "9.2 Danh mục các dòng máy tiêu chuẩn tích hợp sẵn (Brother BAS Series)", level=2)
    add_body_p(doc, 
               "Nhấp vào biểu tượng máy may trên thanh công cụ trên cùng sẽ mở ra hộp thoại 'Machine selection' với các dòng máy tiêu chuẩn:")
    
    add_bullet_item(doc, " Bao gồm các model hàng đầu: BAS-341K, BAS-342K, BAS-365K, BAS-370K (khổ may lên tới 500 x 400 mm, bộ nhớ 20,000 mũi).", bold_prefix="Thẻ K Series:")
    add_bullet_item(doc, " Dành cho các dòng máy may lập trình thế hệ J chuyên dụng.", bold_prefix="Thẻ J Series:")
    add_bullet_item(doc, " Dành cho các dòng máy may công nghiệp tải nặng thế hệ H.", bold_prefix="Thẻ H Series:")
    add_bullet_item(doc, " Thẻ độc quyền mới cho phép tự cấu hình máy may của riêng nhà máy.", bold_prefix="Thẻ Custom:")
    
    add_figure(doc, "final_screenshots/16_machine_selection_dialog.png", 
               "Hình 19: Hộp thoại lựa chọn dòng máy may công nghiệp Brother tiêu chuẩn dòng K, J, H", width=Inches(5.6))
    
    add_custom_heading(doc, "9.3 Hướng dẫn 5 bước tạo và quản lý máy may tùy biến (Manage Custom Machines)", level=2)
    add_body_p(doc, 
               "Quy trình từng bước để tạo một cấu hình máy may tùy biến theo thực tế xưởng sản xuất:")
    
    add_figure(doc, "final_screenshots/17_manage_custom_machines_tab.png", 
               "Hình 20: Thẻ quản lý danh mục máy may tùy biến Manage Custom Machines", width=Inches(5.6))
    
    add_bullet_item(doc, " Trong hộp thoại Machine selection, chuyển sang thẻ 'Custom' rồi nhấp chọn nút 'Manage custom machines'.", bold_prefix="Bước 1 - Truy cập giao diện quản lý:")
    add_bullet_item(doc, " Nhấp nút '+ New' để thêm một thiết bị mới vào danh sách. Nhập tên gọi định danh cho máy tại ô 'Machine name' (ví dụ: 'TEST' hoặc 'BAS342K_CUSTOM_JIG').", bold_prefix="Bước 2 - Tạo hồ sơ và đặt tên máy:")
    add_bullet_item(doc, " Nhập giới hạn vùng may khả dụng của bàn kẹp thực tế: Tọa độ tối đa trục X (ví dụ: 300 mm) và Tọa độ tối đa trục Y (ví dụ: 200 mm hoặc 500 x 400 mm). Điều này đảm bảo hệ thống Out of Sewing Area Detection sẽ kiểm tra chính xác theo khổ may này.", bold_prefix="Bước 3 - Thiết lập kích thước khổ may (X mm, Y mm):")
    add_bullet_item(doc, " Tích chọn các công nghệ phần cứng mà máy may thực tế đang trang bị:\n  • [x] New Tension Code Support: Hỗ trợ mã lực căng chỉ kỹ thuật số mới.\n  • [x] Thickness Detection Support: Hỗ trợ cảm biến phát hiện độ dày vật liệu may.\n  • [x] Mute Needle Bar Base Support: Hỗ trợ cơ cấu trụ kim giảm tiếng ồn khi vận hành.", bold_prefix="Bước 4 - Kích hoạt tính năng công nghệ hỗ trợ (Supported features):")
    add_bullet_item(doc, " Nhấp nút 'Update' để lưu lại cấu hình máy vào bộ nhớ phần mềm. Sau đó nhấp 'Select' để kích hoạt máy này cho tệp dữ liệu may đang thiết kế.", bold_prefix="Bước 5 - Cập nhật và kích hoạt:")
    
    add_figure(doc, "final_screenshots/custom_machine_159s.png", 
               "Hình 21: Cấu hình thông số chi tiết cho máy may tùy biến theo yêu cầu nhà máy (Khổ may X/Y, Tension Code, Thickness Detection)", width=Inches(5.8))
    
    add_callout(doc, 
                "Việc khai báo đúng kích thước khổ may X/Y và tính năng phần cứng của máy tùy biến là yếu tố quyết định để phần mềm tự động ngăn chặn việc kim may đâm vào khung kẹp kim loại và cho phép chèn các mã lệnh điều khiển lực căng chỉ kỹ thuật số chính xác.",
                title="LƯU Ý AN TOÀN THIẾT BỊ", box_type="warning")

    doc.add_page_break()

    # ----------------------------------------------------
    # CHƯƠNG 10: QUY TRÌNH THỰC HÀNH TIÊU CHUẨN (SOP 6 BƯỚC)
    # ----------------------------------------------------
    add_custom_heading(doc, "CHƯƠNG 10: QUY TRÌNH THỰC HÀNH TIÊU CHUẨN (SOP 6 BƯỚC) & HƯỚNG DẪN TRIỂN KHAI", level=1)
    
    add_custom_heading(doc, "10.1 Lưu trình 6 bước chuẩn hóa tạo dữ liệu may từ CAD sang máy Brother", level=2)
    add_body_p(doc, 
               "Nhằm đảm bảo dữ liệu may được tạo ra đạt chất lượng cao nhất và không phát sinh lỗi khi lên chuyền, các nhà máy cần áp dụng quy trình thực hành tiêu chuẩn (SOP) 6 bước sau:")
    
    sop_steps = [
        ("Bước 1: Tiếp nhận và tiền xử lý CAD DXF", "Phòng Rập CAD", "Tiếp nhận bản vẽ rập sản phẩm định dạng DXF từ phòng thiết kế. Kiểm tra tính liên tục của các đường biên và lưu trữ tệp vào thư mục dự án chuẩn."),
        ("Bước 2: Nạp DXF và gán Guide Data", "Kỹ thuật Lập trình", "Mở PS-300C, mở tệp DXF. Tại hộp thoại DXF Import, chọn các Layer cần thiết và ấn định vai trò 'Guide Data' (rập nền tham chiếu) và 'Sewing Data'."),
        ("Bước 3: Biên tập đường may & Lại mũi", "Kỹ thuật Lập trình", "Sử dụng các công cụ trên Floating Dock để vẽ hoặc hiệu chỉnh đường may. Thiết lập chu kỳ và số mũi lại mũi (Back Tack) ở đầu/cuối đường may."),
        ("Bước 4: Kiểm tra lỗi tự động (QA Check)", "Kỹ thuật Lập trình", "Kiểm tra biểu tượng cảnh báo lỗi thời gian thực. Nhấp vào các dòng vi phạm trong bảng Warnings để phần mềm tự zoom và làm sáng đỏ điểm lỗi để sửa chữa."),
        ("Bước 5: Mô phỏng động học & Đánh giá IE", "Kỹ sư IE & Kỹ thuật", "Chuyển sang chế độ Preview, thiết lập Sewing Speed, Feed Speed và Trim Duration. Kiểm tra chuyển động kim và ghi nhận Estimated Sewing Time."),
        ("Bước 6: Chọn cấu hình máy & Xuất tệp", "Trưởng bộ phận Kỹ thuật", "Chọn đúng model máy tiêu chuẩn (K, J, H Series) hoặc máy tùy biến (Custom Machine). Xuất tệp dữ liệu may và chuyển giao ra chuyền sản xuất.")
    ]
    
    tbl_sop = doc.add_table(rows=len(sop_steps) + 1, cols=3)
    tbl_sop.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_sop)
    
    for c, title, w in zip(tbl_sop.rows[0].cells, ["BƯỚC THỰC HIỆN", "TRÁCH NHIỆM", "HÀNH ĐỘNG TIÊU CHUẨN CHI TIẾT"], [Inches(1.8), Inches(1.5), Inches(3.17)]):
        c.width = w
        set_cell_background(c, HEX_PRIMARY)
        set_cell_margins(c, top=100, bottom=100, left=120, right=120)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(title)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    for r_idx, (s_name, s_resp, s_act) in enumerate(sop_steps, start=1):
        row = tbl_sop.rows[r_idx]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width, c1.width, c2.width = Inches(1.8), Inches(1.5), Inches(3.17)
        bg = HEX_LIGHT_BLUE if r_idx % 2 == 1 else "FFFFFF"
        for c in [c0, c1, c2]:
            set_cell_background(c, bg)
            set_cell_margins(c, top=80, bottom=80, left=100, right=100)
            
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(s_name)
        r0.bold = True
        r0.font.name = "Arial"
        r0.font.size = Pt(8.5)
        r0.font.color.rgb = COLOR_SECONDARY
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(s_resp)
        r1.bold = True
        r1.font.name = "Arial"
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = COLOR_PRIMARY
        
        p2 = c2.paragraphs[0]
        p2.paragraph_format.space_after = Pt(0)
        r2 = p2.add_run(s_act)
        r2.font.name = "Arial"
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = COLOR_TEXT

    add_custom_heading(doc, "10.2 Bảng Checklist kiểm tra trước khi chuyển giao dữ liệu xuống xưởng", level=2)
    
    checklist_items = [
        "Đã chọn đúng đơn vị đo lường (mm) và căn giữa bản vẽ CAD DXF?",
        "Các đường rập nền đã được gán chính xác vai trò Guide Data (màu xanh lá)?",
        "Đã thực hiện tối ưu hóa thứ tự may (Optimize Sequence) để giảm thiểu đường chỉ nhảy?",
        "Tất cả các cảnh báo lỗi (Warnings Badge = 0) đã được khắc phục hoàn toàn?",
        "Không có mũi may nào nằm ngoài phạm vi may vật lý của máy (Out of Sewing Area)?",
        "Bước may (Stitch Pitch) tại các đoạn cua cong nằm trong giới hạn an toàn (>= 2.0 mm)?",
        "Đã chạy mô phỏng Playback và kiểm tra thời gian Estimated Sewing Time phù hợp với Cycle Time mục tiêu?",
        "Đã chọn chính xác Model máy thực tế (Tiêu chuẩn hoặc Custom Machine có đúng kích thước X/Y)?"
    ]
    
    for item in checklist_items:
        add_bullet_item(doc, item, bold_prefix="[  ] ")

    add_figure(doc, "final_screenshots/19_brother_core_values_summary.png", 
               "Hình 22: Ba trụ cột nâng cấp đột phá trên phần mềm Brother PS-300C", width=Inches(5.8))
    
    add_custom_heading(doc, "10.3 Lời kết", level=2)
    add_body_p(doc, 
               "Phần mềm Brother PS-300C không chỉ là một bản nâng cấp giao diện đơn thuần, mà là một bước nhảy vọt toàn diện về công nghệ tạo lập dữ liệu may công nghiệp. Với việc kết hợp hoàn hảo giữa giao diện phẳng hiện đại, khả năng bóc tách CAD DXF hai chiều, kiểm soát chất lượng tự động, mô phỏng chu kỳ may thực tế và tính năng tùy biến thiết bị may độ chế linh hoạt (t=146s), PS-300C xứng đáng là chuẩn mực hàng đầu giúp các nhà máy may bứt phá về năng suất, giảm thiểu chi phí và làm chủ hoàn toàn quy trình may tự động hóa.")
    
    output_filename = "Huong_Dan_Su_Dung_Phan_Mem_Brother_PS-300C.docx"
    doc.save(output_filename)
    print(f"Manual successfully saved to: {output_filename}")
    print(f"File size: {os.path.getsize(output_filename)} bytes")

if __name__ == "__main__":
    create_manual()
