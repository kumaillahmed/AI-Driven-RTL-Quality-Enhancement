from fastapi.testclient import TestClient
from rtl_ai.api.main import app
client=TestClient(app)
def test_health():
 assert client.get('/health').status_code==200
