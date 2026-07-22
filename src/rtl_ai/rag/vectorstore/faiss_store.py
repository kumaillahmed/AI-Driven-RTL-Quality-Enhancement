class FAISSStore:
 def __init__(self): self.index=[]
 def add(self,v,m): self.index.append((v,m))
 def search(self,q,k=3): return self.index[:k]
