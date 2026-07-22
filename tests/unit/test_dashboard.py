from rtl_ai.dashboard.utils.api_client import analyze_log

def test_api():
    assert "summary" in analyze_log("test")
