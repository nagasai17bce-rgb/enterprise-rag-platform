from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").status_code == 200

def test_citations():
    data = client.post("/v1/run", json={"value": "incident response"}).json()
    assert data["results"][0]["citation"]
