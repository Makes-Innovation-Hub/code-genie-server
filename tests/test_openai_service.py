import os
import requests

def test_openai_endpoint():
    server_url = os.getenv("SERVER_URL")
    url = f"{server_url}/question/test"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(
        response.text, str) == True
    assert response.text.lower().replace('"', '') == "hello"
    
def test_basic_question_generation():
    server_url = os.getenv("SERVER_URL")
    url = f"{server_url}/question/basic"
    response = requests.post(url,json={"topic":"python"})
    assert response.status_code == 200
    answer = response.json()
    assert "question" in answer
    assert "answer" in answer
    assert "python" in answer["question"].lower()
    