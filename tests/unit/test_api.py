from rtl_ai.api.services.analyzer import analyze_log

def test_analyze():
    result=analyze_log("test")
    assert "summary" in result
