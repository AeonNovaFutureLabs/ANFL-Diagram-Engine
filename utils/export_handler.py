import io
from typing import Dict
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class ExportHandler:
    @staticmethod
    def create_pdf(diagrams: str) -> bytes:
        """Generate styled PDF with diagrams."""
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()

        # Custom style for diagrams
        diagram_style = ParagraphStyle(
            'DiagramStyle',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            leading=14,
            textColor=colors.HexColor('#1A1A2E'),
            backColor=colors.HexColor('#E6E6E6'),
            borderPadding=10,
            borderColor=colors.HexColor('#CD7F32'),
            borderWidth=1,
        )

        elements = []
        for diagram in diagrams.split('\n\n'):
            elements.append(Paragraph(diagram, diagram_style))

        doc.build(elements)
        buffer.seek(0)
        return buffer.getvalue()

    @staticmethod
    def to_notion_markdown(diagrams: str) -> str:
        """Convert to Notion-compatible markdown."""
        return f"```mermaid\n{diagrams}\n```"

    @staticmethod
    def create_latex(diagrams: str) -> str:
        """Generate LaTeX document with TikZ diagrams."""
        from utils.latex_converter import LaTeXConverter
        return LaTeXConverter.mermaid_to_tikz(diagrams)