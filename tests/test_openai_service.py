import os
import requests

from services.openai_service import get_question_and_answer

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

def test_generate_question_with_difficaulty():
    q_n_a_dict = get_question_and_answer(topic="python",difficulty='hard')
    assert "question" in q_n_a_dict
    assert "answer" in q_n_a_dict
    assert q_n_a_dict["difficulty"] == 'hard'
    
def test_question_generation_fail():
    # testing send req without topic - should fail with 422
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    url = f"{server_url}/question/basic"
    response = requests.post(url)
    assert response.status_code == 422
    
def test_question_generation_fail_with_diff():
    # testing send req without topic with difficulty - should fail with 422
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    url = f"{server_url}/question/basic"
    response = requests.post(url,json={"difficulty":"hard"})
    assert response.status_code == 422

def test_question_generation_wrong_difficulty():
    # testing send req with wrong value for difficulty
    # i.e - not ["easy","medium","hard","very hard"] | None
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    url = f"{server_url}/question/basic"
    response = requests.post(url,json={"topic":"python","difficulty":"fake"})
    assert response.status_code == 422
    response = requests.post(url,json={"topic":"python","difficulty":"super hard"})
    assert response.status_code == 422