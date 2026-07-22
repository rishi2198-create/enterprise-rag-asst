from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:
    """
    Generates embeddings for text chunks.
    """

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def generate_embeddings(self, chunks):
        """
        Convert text chunks into embeddings.
        """

        embeddings = self.model.encode(
            chunks,
            show_progress_bar=True
        )

        return embeddings