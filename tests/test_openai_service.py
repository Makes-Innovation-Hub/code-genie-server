import os
import requests
import pytest

def test_openai_endpoint():
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    url = f"{server_url}/question/test"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(
        response.text, str) == True
    assert response.text.lower().replace('"', '') == "hello"

def test_question_generation_endpoint():
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    url = f"{server_url}/question/basic"
    response = requests.post(url,json={"topic":"python"})
    assert response.status_code == 200
    answer = response.json()
    assert "question" in answer
    assert "answer" in answer
    assert "python" in answer["question"].lower()

def test_question_generation_fail():
    # testing send req without topic - should fail with 422
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    url = f"{server_url}/question/basic"
    response = requests.post(url)
    assert response.status_code == 422