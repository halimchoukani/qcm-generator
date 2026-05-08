# pdf_generator.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class PDFGenerator:
    def __init__(self, config):
        self.output_path = config.output_pdf_path

    def generate(self, questions):
        c = canvas.Canvas(self.output_path, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "QCM Correction")
        y = 700
        for i, q in enumerate(questions, start=1):
            c.drawString(100, y, f"{i}. {q['question']}")
            y -= 20
            c.drawString(120, y, f"Correct Answer: {q['correct']}")
            y -= 40
            if y < 100:
                c.showPage()
                y = 750
        c.save()
