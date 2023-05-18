from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_items():
    response = client.get("/items/5")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": None}


def test_read_items_q():
    response = client.get("/items/5?q=hello")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": "hello"}