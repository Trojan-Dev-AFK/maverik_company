import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture
def token():
    client.post("/auth/register", json={"username": "tester", "password": "secret123"})
    resp = client.post(
        "/auth/login", json={"username": "tester", "password": "secret123"}
    )
    assert resp.status_code == 200
    return resp.json()["access_token"]


def test_items_requires_auth():
    resp = client.get("/items/")
    assert resp.status_code == 401
    assert resp.json()["detail"] == "Not authenticated"


def test_create_item(token):
    headers = {"Authorization": f"Bearer {token}"}
    resp = client.post("/items/", json={"name": "Pen", "price": 1.5}, headers=headers)
    assert resp.status_code == 201
    data = resp.json()
    assert data["name"] == "Pen"
    assert "id" in data


def test_read_item(token):
    headers = {"Authorization": f"Bearer {token}"}
    create_resp = client.post(
        "/items/", json={"name": "Book", "price": 10.0}, headers=headers
    )
    item_id = create_resp.json()["id"]
    resp = client.get(f"/items/{item_id}", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["id"] == item_id


def test_update_item(token):
    headers = {"Authorization": f"Bearer {token}"}
    create_resp = client.post(
        "/items/", json={"name": "Pencil", "price": 0.5}, headers=headers
    )
    item_id = create_resp.json()["id"]
    resp = client.put(
        f"/items/{item_id}", json={"name": "HB Pencil", "price": 0.75}, headers=headers
    )
    assert resp.status_code == 200
    assert resp.json()["name"] == "HB Pencil"


def test_delete_item(token):
    headers = {"Authorization": f"Bearer {token}"}
    create_resp = client.post(
        "/items/", json={"name": "Eraser", "price": 0.3}, headers=headers
    )
    item_id = create_resp.json()["id"]
    resp = client.delete(f"/items/{item_id}", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["message"] == "Item deleted"
    resp2 = client.get(f"/items/{item_id}", headers=headers)
    assert resp2.status_code == 404
