from rtl_ai.rag.embeddings.embedder import Embedder
from rtl_ai.rag.vectorstore.faiss_store import FAISSStore
class RetrievalPipeline:
 def __init__(self): self.e=Embedder(); self.db=FAISSStore()
