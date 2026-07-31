from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["application"] == "app-demo"


def test_ready_endpoint():
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"


def test_info_endpoint():
    response = client.get("/info")
    body = response.json()
    assert response.status_code == 200
    assert body["application"] == "app-demo"
    assert body["version"] == "0.1.0"
    assert body["environment"] == "local"
    assert "hostname" in body
    assert "timestamp" in body


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "Aplicación disponible" in response.text
    assert "app-demo" in response.text
