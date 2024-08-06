import os
import requests
import json

req_post_headers = {
    "content-type":"application/json"
}

def test_question_generation_endpoint():
    # test only with topic param
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    url = f"{server_url}/question/generate"
    response = requests.post(url,json={"topic":"python"})
    assert response.status_code == 200
    q_n_a_dict = response.json()
    assert "Question" in q_n_a_dict
    assert "Answer" in q_n_a_dict
    assert "Explanations" in q_n_a_dict
    assert "difficulty" not in q_n_a_dict
    assert len(q_n_a_dict["Answer"]) == 1
    assert len(q_n_a_dict["Explanations"]) == 1

def test_generate_question_with_difficaulty():
    # req with topic and difficulty - no answers num
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    url = f"{server_url}/question/generate"
    response = requests.post(url,json={"topic":"python","difficulty":"hard"})
    assert response.status_code == 200
    q_n_a_dict = response.json()
    assert "Question" in q_n_a_dict
    assert "Answer" in q_n_a_dict
    assert "Explanations" in q_n_a_dict
    assert q_n_a_dict["difficulty"] == 'hard'
    
def test_question_generation_fail():
    # testing send req without topic - should fail with 422
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    url = f"{server_url}/question/generate"
    response = requests.post(url)
    assert response.status_code == 422
    
def test_question_generation_fail_with_diff():
    # testing send req without topic with difficulty - should fail with 422
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    url = f"{server_url}/question/generate"
    response = requests.post(url,json={"difficulty":"hard"})
    assert response.status_code == 422

def test_question_generation_wrong_difficulty():
    # testing send req with wrong value for difficulty
    # i.e - not ["easy","medium","hard","very hard"] | None
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    url = f"{server_url}/question/generate"
    response = requests.post(url,json={"topic":"python","difficulty":"fake"})
    assert response.status_code == 422
    response = requests.post(url,json={"topic":"python","difficulty":"super hard"})
    assert response.status_code == 422
    response = requests.post(url,json={"topic":"python","difficulty":"HARD"})
    assert response.status_code == 422
    
def test_gen_question_answers_num():
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    answers_num = 3
    url = f"{server_url}/question/generate"
    response = requests.post(
        url,
        json={"topic":"python",
              "answers_num":answers_num
        },
        headers=req_post_headers,
        timeout=50000
        )
    assert response.status_code == 200
    q_n_a_dict = response.json()
    if isinstance(q_n_a_dict,str):
        q_n_a_dict = json.dumps(response.json())
    assert isinstance(q_n_a_dict, dict)
    assert "Question" in q_n_a_dict
    assert "Answer" in q_n_a_dict
    assert "Explanations" in q_n_a_dict
    assert "difficulty" not in q_n_a_dict
    assert len(q_n_a_dict["Answer"]) == answers_num
    assert len(q_n_a_dict["Explanations"]) == answers_num
    
def test_gen_multiple_answers_and_difficulty():
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    answers_num = 3
    url = f"{server_url}/question/generate"
    response = requests.post(
        url,
        json={"topic":"python",
              "answers_num":answers_num,
              "difficulty": "easy"
        },
        headers=req_post_headers,
        timeout=50000
        )
    assert response.status_code == 200
    q_n_a_dict = response.json()
    if isinstance(q_n_a_dict,str):
        q_n_a_dict = json.dumps(response.json())
    assert isinstance(q_n_a_dict, dict)
    assert "Question" in q_n_a_dict
    assert "Answer" in q_n_a_dict
    assert "Explanations" in q_n_a_dict
    assert "difficulty" in q_n_a_dict
    assert len(q_n_a_dict["Answer"]) == answers_num
    assert len(q_n_a_dict["Explanations"]) == answers_num