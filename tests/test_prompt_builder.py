from rtl_ai.llm.prompt_builder import build_prompt

def test_prompt():
    p = build_prompt("CDC issue","Two-flop synchronizer")
    assert "CDC issue" in p
