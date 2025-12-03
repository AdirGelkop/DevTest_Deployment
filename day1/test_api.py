import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user_returns_200():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200

def test_get_user_has_name():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert "name" in data

def test_create_user_returns_201():
    new_user = {"name": "Test", "email": "test@test.com"}
    response = requests.post(f"{BASE_URL}/users", json=new_user)
    assert response.status_code == 201

def test_get_nonexistent_user_returns_404():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404