class VectorStore:
 def __init__(self): self.items=[]
 def add(self,v,m): self.items.append((v,m))
 def search(self,q,k=3): return self.items[:k]
