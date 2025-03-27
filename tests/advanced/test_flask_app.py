import pytest
from projects.advanced.flask_app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_user_success(client):
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json == {"name": "Alice", "age": 25}

def test_get_user_not_found(client):
    response = client.get("/user/99")
    assert response.status_code == 404
    assert response.json == {"error": "User not found"}
