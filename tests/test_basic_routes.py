import requests
import os

def test_root():
    server_url = os.getenv('SERVER_URL')
    assert server_url is not None
    response = requests.get(server_url)
    assert response.status_code == 200
    assert response.json() == 'Hello from FastAPI server'