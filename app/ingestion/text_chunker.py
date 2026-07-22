from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextChunker:
    """Splits text into chunks for embedding."""

    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split_text(self, text: str):
        """Split text into chunks."""
        return self.text_splitter.split_text(text)