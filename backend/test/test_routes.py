from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_crawl_endpoint_with_valid_url():
    response = client.get("/pages?target=https://filip-ph-johansson.github.io/")
    assert response.status_code == 200
    data = response.json()
    assert "pages" in data
    assert isinstance(data["pages"], list)
    assert "domain" in data
    assert isinstance(data["domain"], str)