from rtl_ai.pipeline.llm_pipeline import run

def test_pipeline():
    assert "Mock Response" in run("Unused signal","RTL guideline")
