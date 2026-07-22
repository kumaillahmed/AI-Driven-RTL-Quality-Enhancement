from rtl_ai.api.models.requests import AnalysisRequest
def test_req():
 assert AnalysisRequest(issue='CDC').issue=='CDC'
