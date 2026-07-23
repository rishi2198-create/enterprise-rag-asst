import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.vector_store.qdrant_client import QdrantManager

manager = QdrantManager()
client = manager.get_client()

print("=" * 60)
print("Attempting to connect to Qdrant Database...")
print("=" * 60)

print("\nConnected to Qdrant!")
print("\nActive Collections:")
print(client.get_collections())
