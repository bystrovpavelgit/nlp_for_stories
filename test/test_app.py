""" test web-app """
from fastapiapp.main_app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health_check():
    """ test root page """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"NLP": "App"}
