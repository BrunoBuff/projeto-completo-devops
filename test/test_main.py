import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_response_json():
    response = client.get("/")
    assert response.json() == {"Mensagem": "Deu certo"}


def test_response_type():
    response = client.get("/")
    assert isinstance(response.json(), dict)


def test_message_exists():
    response = client.get("/")
    assert "Mensagem" in response.json()


def test_message_content():
    response = client.get("/")
    assert response.json()["Mensagem"] == "Deu certo"