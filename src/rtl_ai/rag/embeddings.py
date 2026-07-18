class EmbeddingModel:
 def embed(self,text):
  return [len(text), sum(map(ord,text))%1000]
