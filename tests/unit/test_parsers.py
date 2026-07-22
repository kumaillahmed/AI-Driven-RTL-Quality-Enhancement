from rtl_ai.parser.unified_parser import UnifiedParser

def test_lint():
    p=UnifiedParser()
    assert len(p.parse("lint","LINT001 test"))==1

def test_cdc():
    p=UnifiedParser()
    assert len(p.parse("cdc","CDC001 test"))==1

def test_rdc():
    p=UnifiedParser()
    assert len(p.parse("rdc","RDC001 test"))==1
