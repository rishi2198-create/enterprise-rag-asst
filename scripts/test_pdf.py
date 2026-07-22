import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ingestion.pdf_handler import PDFHandler

pdf = PDFHandler()

text = pdf.extract_text("data/raw/sample.pdf")

print("=" * 60)
print("PDF Loaded Successfully!")
print("=" * 60)

print(f"\nCharacters Extracted: {len(text)}")

print("\nFirst 500 Characters:\n")

print(text[:500])
