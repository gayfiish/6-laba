from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Привет, FastAPI!"}


def test_greet():
    response = client.get("/greet", params={"name": "Анастасия"})
    assert response.status_code == 200
    assert response.json() == {"message": "Привет, Анастасия!"}


def test_greet_another_name():
    response = client.get("/greet", params={"name": "Иван"})
    assert response.status_code == 200
    assert response.json() == {"message": "Привет, Иван!"}


def test_greet_without_name():
    response = client.get("/greet")
    assert response.status_code == 422