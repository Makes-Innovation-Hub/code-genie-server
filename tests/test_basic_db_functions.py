from fastapi.testclient import TestClient
from server import app
import re

client = TestClient(app)

def test_test_store_in_mongodb():
    response = client.get('/test/')
    assert response.status_code == 200
    # Make sure that the returned follows the pattern: 'number' was stored successfully
    pattern = r'^\d+ was stored successfully$'
    assert re.match(pattern, response.json()), 'Response does not match the expected pattern'
    # Make sure the number that was inserted is between 0 and 1000
    assert 0 < int(response.json().split()[0]) < 1000
