# Create test cases for the /generate route in main.py using FastAPI TestClient
from fastapi.testclient import TestClient
from main import app  # This imports your app from main.py

client = TestClient(app)

def test_generate_checksum():
    # Sending a sample JSON body
    payload = {"text": "hello world"}
    response = client.post("/generate", json=payload)
    
    # Assertions to verify the result
    assert response.status_code == 200
    assert "checksum" in response.json()
    assert "Welcome" in response.json()["message"]
