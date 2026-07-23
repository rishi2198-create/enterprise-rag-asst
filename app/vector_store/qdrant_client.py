from qdrant_client import QdrantClient

class QdrantManager:
    """Manages connection to Qdrant."""

    def __init__(self):
        self.client = QdrantClient(
            host="localhost",
            port=6333
        )

    def get_client(self):
        return self.client