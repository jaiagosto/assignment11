# tests/integration/test_fastapi_calculator.py

import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    """Pytest Fixture to create a TestClient for the FastAPI application."""
    with TestClient(app) as client:
        yield client


def test_add_api(client):
    """Test the Addition API Endpoint."""
    response = client.post('/add', json={'a': 10, 'b': 5})
    assert response.status_code == 200
    assert response.json()['result'] == 15


def test_subtract_api(client):
    """Test the Subtraction API Endpoint."""
    response = client.post('/subtract', json={'a': 10, 'b': 5})
    assert response.status_code == 200
    assert response.json()['result'] == 5


def test_multiply_api(client):
    """Test the Multiplication API Endpoint."""
    response = client.post('/multiply', json={'a': 10, 'b': 5})
    assert response.status_code == 200
    assert response.json()['result'] == 50


def test_divide_api(client):
    """Test the Division API Endpoint."""
    response = client.post('/divide', json={'a': 10, 'b': 2})
    assert response.status_code == 200
    assert response.json()['result'] == 5


def test_divide_by_zero_api(client):
    """Test the Division by Zero API Endpoint."""
    response = client.post('/divide', json={'a': 10, 'b': 0})
    assert response.status_code == 400
    assert 'error' in response.json()
    assert "Cannot divide by zero!" in response.json()['error']