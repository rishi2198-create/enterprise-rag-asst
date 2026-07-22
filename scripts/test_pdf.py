import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ingestion.pdf_handler import PDFHandler
from app.ingestion.text_chunker import TextChunker

pdf = PDFHandler()
chunker = TextChunker()

text = pdf.extract_text("data/raw/sample.pdf")

chunks = chunker.split_text(text)

print("=" * 60)
print("PDF Loaded Successfully!")
print("=" * 60)

print(f"\nCharacters Extracted: {len(text)}")
print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])

print("\nSecond Chunk:\n")
print(chunks[1])
