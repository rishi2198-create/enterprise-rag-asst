import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ingestion.pdf_handler import PDFHandler
from app.ingestion.text_chunker import TextChunker
from app.embeddings.embedding_generator import EmbeddingGenerator

# Initialize components
pdf = PDFHandler()
chunker = TextChunker()
embedder = EmbeddingGenerator()

# Process PDF into chunks
text = pdf.extract_text("data/raw/sample.pdf")
chunks = chunker.split_text(text)

# Generate vector embeddings
embeddings = embedder.generate_embeddings(chunks)

print("=" * 60)
print("PDF Ingestion & Embeddings Test Successful!")
print("=" * 60)

print(f"\nCharacters Extracted: {len(text)}")
print(f"Total Chunks Created: {len(chunks)}")
print(f"Number of Embeddings: {len(embeddings)}")
print(f"Embedding Dimension: {len(embeddings[0])}")

