from pathlib import Path

def load_documents(folder):
 docs=[]
 for f in Path(folder).glob('*.md'):
  docs.append({'source':f.name,'text':f.read_text(encoding='utf-8')})
 return docs
