# -*- coding: utf-8 -*-
"""
Script to generate the comprehensive, professional .docx manual for Brother PS-300C
Sewing Data Creation Software.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

# --- Color Palette Constants (Brother Industrial Theme) ---
COLOR_PRIMARY = RGBColor(0, 91, 172)     # Brother Blue (#005BAC)
COLOR_SECONDARY = RGBColor(30, 41, 59)   # Dark Slate (#1E293B)
COLOR_TEXT = RGBColor(51, 65, 85)        # Slate Text (#334155)
COLOR_MUTED = RGBColor(100, 116, 139)    # Muted Gray (#64748B)
COLOR_RED = RGBColor(185, 28, 28)        # Warning Red (#B91C1C)
COLOR_GREEN = RGBColor(5, 150, 105)      # Tip Green (#059669)

HEX_PRIMARY = "005BAC"
HEX_SECONDARY = "1E293B"
HEX_LIGHT_BLUE = "F0F7FD"
HEX_LIGHT_GREEN = "ECFDF5"
HEX_LIGHT_AMBER = "FFFBEB"
HEX_LIGHT_GRAY = "F8FAFC"
HEX_BORDER = "CBD5E1"
HEX_BORDER_DARK = "94A3B8"

def set_cell_background(cell, hex_color):
    """Sets background shading of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    """Sets internal cell margins in DXA."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    """Applies clean borders to a table."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:left w:val="none"/>
            <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:right w:val="none"/>
            <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def add_header_footer(doc):
    """Adds running headers and footers with page numbers."""
    section = doc.sections[0]
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.9)
    section.right_margin = Inches(0.9)
    section.page_width = Inches(8.27)   # A4 width
    section.page_height = Inches(11.69) # A4 height

    # Header
    header = section.header
    header_p = header.paragraphs[0]
    header_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_h = header_p.add_run("BROTHER PS-300C | SỔ TAY HƯỚNG DẪN KỸ THUẬT VÀ LẬP TRÌNH DỮ LIỆU MAY")
    run_h.font.name = "Arial"
    run_h.font.size = Pt(8.5)
    run_h.font.color.rgb = COLOR_MUTED

    # Footer
    footer = section.footer
    footer_p = footer.paragraphs[0]
    footer_p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_f1 = footer_p.add_run("Brother Asia Industrial Sewing Machine • Tài liệu kỹ thuật chuẩn hóa")
    run_f1.font.name = "Arial"
    run_f1.font.size = Pt(8.5)
    run_f1.font.color.rgb = COLOR_MUTED

def add_custom_heading(doc, text, level, space_before=16, space_after=6):
    """Adds a styled heading with controlled spacing and color."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.keep_with_next = True
    
    run = p.add_run(text)
    run.bold = True
    run.font.name = "Arial"
    
    if level == 1:
        run.font.size = Pt(17)
        run.font.color.rgb = COLOR_PRIMARY
        # Add a subtle bottom border or separator line
        pBdr = parse_xml(f'''
            <w:pBdr {nsdecls("w")}>
                <w:bottom w:val="single" w:sz="12" w:space="4" w:color="{HEX_PRIMARY}"/>
            </w:pBdr>
        ''')
        p._p.get_or_add_pPr().append(pBdr)
    elif level == 2:
        run.font.size = Pt(13.5)
        run.font.color.rgb = COLOR_SECONDARY
    elif level == 3:
        run.font.size = Pt(11.5)
        run.font.color.rgb = COLOR_PRIMARY
    return p

def add_body_p(doc, text="", bold_prefix="", space_after=6, line_spacing=1.15):
    """Adds a standard body paragraph."""
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = "Arial"
        r_pre.font.size = Pt(10)
        r_pre.font.color.rgb = COLOR_SECONDARY
        
    if text:
        r_text = p.add_run(text)
        r_text.font.name = "Arial"
        r_text.font.size = Pt(10)
        r_text.font.color.rgb = COLOR_TEXT
    return p

def add_bullet_item(doc, text, bold_prefix="", level=0):
    """Adds a bullet list item."""
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = "Arial"
        r_pre.font.size = Pt(10)
        r_pre.font.color.rgb = COLOR_SECONDARY
    r_text = p.add_run(text)
    r_text.font.name = "Arial"
    r_text.font.size = Pt(10)
    r_text.font.color.rgb = COLOR_TEXT
    return p

def add_callout(doc, text, title="LƯU Ý QUAN TRỌNG", box_type="note"):
    """Creates a professional callout box with colored left border and light shading."""
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.47)
    
    if box_type == "note":
        bg_color = HEX_LIGHT_BLUE
        border_color = HEX_PRIMARY
        title_color = COLOR_PRIMARY
        icon = "📌"
    elif box_type == "tip":
        bg_color = HEX_LIGHT_GREEN
        border_color = "059669"
        title_color = COLOR_GREEN
        icon = "💡"
    elif box_type == "warning":
        bg_color = HEX_LIGHT_AMBER
        border_color = "D97706"
        title_color = RGBColor(217, 119, 6)
        icon = "⚠️"
    elif box_type == "ie":
        bg_color = "F5F3FF"
        border_color = "7C3AED"
        title_color = RGBColor(124, 58, 237)
        icon = "⚙️"
    else:
        bg_color = HEX_LIGHT_GRAY
        border_color = HEX_BORDER_DARK
        title_color = COLOR_SECONDARY
        icon = "ℹ️"
        
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    # Left border only
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>
            <w:top w:val="none"/>
            <w:right w:val="none"/>
            <w:bottom w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    r_title = p.add_run(f"{icon} {title}\n")
    r_title.bold = True
    r_title.font.name = "Arial"
    r_title.font.size = Pt(10)
    r_title.font.color.rgb = title_color
    
    r_content = p.add_run(text)
    r_content.font.name = "Arial"
    r_content.font.size = Pt(9.5)
    r_content.font.color.rgb = COLOR_TEXT
    
    # Empty space after table
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_after = Pt(6)

def add_figure(doc, image_path, caption_text, width=Inches(5.8)):
    """Inserts a centered image with a professional caption below it."""
    if not os.path.exists(image_path):
        print(f"Warning: image not found {image_path}")
        return
        
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(10)
    p_img.paragraph_format.space_after = Pt(4)
    p_img.paragraph_format.keep_with_next = True
    
    run_img = p_img.add_run()
    run_img.add_picture(image_path, width=width)
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(0)
    p_cap.paragraph_format.space_after = Pt(12)
    
    r_cap = p_cap.add_run(caption_text)
    r_cap.font.name = "Arial"
    r_cap.font.size = Pt(9)
    r_cap.italic = True
    r_cap.font.color.rgb = COLOR_MUTED

print("Base helper definitions loaded successfully.")
