"""
EduTrack AI - PDF Generator Utility
Generates clean, valid PDF documents for subjects and academic tasks
without requiring external third-party dependencies.
"""

import unicodedata
from typing import List, Dict, Any
from datetime import datetime


def _sanitize_text(text: str) -> str:
    """Normalize text to ASCII/Latin-1 safe characters for standard PDF fonts."""
    if not text:
        return ""
    # Normalize unicode characters to closest ASCII equivalent (e.g. ã -> a, é -> e)
    normalized = unicodedata.normalize('NFKD', str(text)).encode('ASCII', 'ignore').decode('ASCII')
    # Escape special PDF characters: (, ), \
    escaped = (
        normalized.replace("\\", "\\\\")
                  .replace("(", "\\(")
                  .replace(")", "\\)")
    )
    return escaped


def build_pdf_document(title: str, subtitle: str, metadata: Dict[str, str], sections: List[Dict[str, Any]]) -> bytes:
    """
    Build a standard PDF 1.4 document in pure Python.
    
    :param title: Main document title (e.g., 'EduTrack AI - Resumo de Disciplina')
    :param subtitle: Document subtitle or timestamp
    :param metadata: Key-value pairs for general info (e.g. {'Disciplina': 'Calculo I', 'Professor': 'Dr. Silva'})
    :param sections: List of sections, e.g. [{'title': 'Tarefas Associadas', 'items': [...]}]
    :return: PDF file content as bytes.
    """
    stream_lines = []
    
    # Helper to add text stream instructions
    # Coordinate system: origin (0, 0) at bottom-left. A4 is 595.28 x 841.89 points.
    y = 800
    
    # Header background bar (dark blue)
    stream_lines.append("0.12 0.23 0.38 rg") # fill color #1F3B61
    stream_lines.append(f"40 {y - 45} 515 55 re f")
    
    # Header title (white, bold)
    stream_lines.append("1.0 1.0 1.0 rg") # white
    stream_lines.append("BT")
    stream_lines.append("/F2 20 Tf") # Helvetica-Bold 20
    stream_lines.append(f"55 {y - 20} Td")
    stream_lines.append(f"({_sanitize_text(title)}) Tj")
    stream_lines.append("ET")
    
    # Subtitle (light gray)
    if subtitle:
        stream_lines.append("0.85 0.88 0.92 rg")
        stream_lines.append("BT")
        stream_lines.append("/F1 10 Tf")
        stream_lines.append(f"55 {y - 38} Td")
        stream_lines.append(f"({_sanitize_text(subtitle)}) Tj")
        stream_lines.append("ET")
        
    y -= 75
    
    # Metadata Box
    if metadata:
        stream_lines.append("0.95 0.96 0.98 rg") # Light background
        stream_lines.append(f"40 {y - (len(metadata) * 20 + 15)} 515 {len(metadata) * 20 + 15} re f")
        
        # Border
        stream_lines.append("0.8 0.83 0.88 RG")
        stream_lines.append("1 w")
        stream_lines.append(f"40 {y - (len(metadata) * 20 + 15)} 515 {len(metadata) * 20 + 15} re S")
        
        y -= 20
        for key, val in metadata.items():
            stream_lines.append("0.1 0.1 0.1 rg")
            stream_lines.append("BT")
            stream_lines.append("/F2 11 Tf") # Bold key
            stream_lines.append(f"55 {y} Td")
            stream_lines.append(f"({_sanitize_text(key)}:) Tj")
            stream_lines.append("ET")
            
            stream_lines.append("0.25 0.25 0.25 rg")
            stream_lines.append("BT")
            stream_lines.append("/F1 11 Tf") # Regular val
            stream_lines.append(f"160 {y} Td")
            stream_lines.append(f"({_sanitize_text(val)}) Tj")
            stream_lines.append("ET")
            y -= 20
            
        y -= 25

    # Sections (e.g. Tasks list)
    for section in sections:
        sec_title = section.get("title", "")
        items = section.get("items", [])
        
        # Section Header
        stream_lines.append("0.12 0.23 0.38 rg")
        stream_lines.append("BT")
        stream_lines.append("/F2 14 Tf")
        stream_lines.append(f"40 {y} Td")
        stream_lines.append(f"({_sanitize_text(sec_title)}) Tj")
        stream_lines.append("ET")
        
        # Underline
        stream_lines.append("0.12 0.23 0.38 RG")
        stream_lines.append("1.5 w")
        stream_lines.append(f"40 {y - 4} m 555 {y - 4} l S")
        
        y -= 25
        
        if not items:
            stream_lines.append("0.5 0.5 0.5 rg")
            stream_lines.append("BT")
            stream_lines.append("/F1 10 Tf")
            stream_lines.append(f"55 {y} Td")
            stream_lines.append("(Nenhum item registrado para esta secao.) Tj")
            stream_lines.append("ET")
            y -= 25
        else:
            for item in items:
                if y < 80: # Avoid drawing off-page
                    break
                    
                # Bullet circle
                stream_lines.append("0.2 0.4 0.6 rg")
                stream_lines.append(f"48 {y + 3} 3 0 360 arc f") # In PDF syntax, simple small rect:
                stream_lines.append(f"47 {y + 2} 4 4 re f")
                
                # Item main text
                item_header = item.get("header", "")
                item_detail = item.get("detail", "")
                
                stream_lines.append("0.15 0.15 0.15 rg")
                stream_lines.append("BT")
                stream_lines.append("/F2 10 Tf")
                stream_lines.append(f"58 {y} Td")
                stream_lines.append(f"({_sanitize_text(item_header)}) Tj")
                stream_lines.append("ET")
                
                if item_detail:
                    stream_lines.append("0.4 0.4 0.4 rg")
                    stream_lines.append("BT")
                    stream_lines.append("/F1 9 Tf")
                    stream_lines.append(f"58 {y - 13} Td")
                    stream_lines.append(f"({_sanitize_text(item_detail)}) Tj")
                    stream_lines.append("ET")
                    y -= 30
                else:
                    y -= 20

    # Footer
    stream_lines.append("0.5 0.5 0.5 rg")
    stream_lines.append("BT")
    stream_lines.append("/F1 8 Tf")
    stream_lines.append("40 30 Td")
    gen_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    stream_lines.append(f"(EduTrack AI - Gerado automaticamente em {gen_time}) Tj")
    stream_lines.append("ET")
    
    # Border line above footer
    stream_lines.append("0.85 0.85 0.85 RG")
    stream_lines.append("0.5 w")
    stream_lines.append("40 42 m 555 42 l S")

    content_stream = "\n".join(stream_lines).encode("latin1", errors="replace")
    
    # PDF Object Construction
    objects = []
    
    # 1: Catalog
    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    # 2: Pages
    objects.append(b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
    # 3: Page
    objects.append(
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595.28 841.89] "
        b"/Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> >>"
    )
    # 4: Contents Stream
    objects.append(
        b"<< /Length " + str(len(content_stream)).encode("ascii") + b" >>\nstream\n" +
        content_stream + b"\nendstream"
    )
    # 5: Font F1 (Helvetica)
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    # 6: Font F2 (Helvetica-Bold)
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")
    
    # Build complete PDF bytes with xref
    header = b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
    body = bytearray(header)
    offsets = [0] # 0 obj offset
    
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(body))
        body.extend(f"{i} 0 obj\n".encode("ascii"))
        body.extend(obj)
        body.extend(b"\nendobj\n")
        
    xref_offset = len(body)
    body.extend(f"xref\n0 {len(offsets)}\n".encode("ascii"))
    body.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        body.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
        
    body.extend(b"trailer\n")
    body.extend(f"<< /Size {len(offsets)} /Root 1 0 R >>\n".encode("ascii"))
    body.extend(b"startxref\n")
    body.extend(f"{xref_offset}\n".encode("ascii"))
    body.extend(b"%%EOF\n")
    
    return bytes(body)
