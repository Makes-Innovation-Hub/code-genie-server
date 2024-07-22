import re

import requests
from fastapi.testclient import TestClient
from server import app

client = TestClient(app)


def test_store_data():
    data = {
        'question': 'Are you mad?',
        'answer': 'No',
        'explanation': 'I am happy',
        'difficulty': 'easy',
        'user_name': 'basil',
        'user_id': '12'
    }
    response = client.post('/questions/store-data/', data=data)
    assert response.status_code == 200
    # This pattern represent the response that must be sent
    pattern = r"^Question: '([^']+)\?'\. ([^']+) of id ([^']+) answer: '([^']+)'\. Explanation: '([^']+)'$"
    assert re.match(pattern, response.json()), 'Response does not match the expected pattern'


def test_generate_question():
    response = client.post('/questions/generate-question/')
    assert response.status_code == 200
    pattern = r"^.*\?$"
    assert re.match(pattern, response.json()), 'Response does not match the expected pattern'
