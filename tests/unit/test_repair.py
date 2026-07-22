from rtl_ai.llm.repair.rtl_repair import repair

def test_repair():
    assert 'Suggested' in repair('module x; endmodule','CDC')
