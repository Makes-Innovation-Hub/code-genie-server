from fastapi.testclient import TestClient
from dotenv import load_dotenv
from server import app
import requests
import os

load_dotenv()

client = TestClient(app)
server_url = os.getenv('SERVER_URL')

def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == 'Hello from FastAPI server'

def test_remote_root():
    # Note that we used requests.get instead of client.get
    response = requests.get(server_url)
    assert response.status_code == 200
    assert response.json() == 'Hello from FastAPI server'
