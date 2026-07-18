from .embeddings import EmbeddingModel
from .vector_store import VectorStore
class Retriever:
 def __init__(self):
  self.embedder=EmbeddingModel(); self.store=VectorStore()
