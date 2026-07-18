from rtl_ai.rag.chunker import chunk_text

def test_chunker():
 assert len(chunk_text('abcdef',3))==2
