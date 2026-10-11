import pytest
from app import app

@pytest.fixture()
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_home_page(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"Student DevOps Task Manager" in r.data

def test_health(client):
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.json["status"] == "healthy"

def test_add_task(client):
    r = client.post("/add", data={"title":"Test CI/CD"}, follow_redirects=True)
    assert r.status_code == 200
    assert b"Test CI/CD" in r.data
