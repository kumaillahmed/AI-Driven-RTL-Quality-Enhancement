from pathlib import Path

def load_docs(folder):
 return [p.read_text(encoding='utf-8') for p in Path(folder).glob('*.md')]
