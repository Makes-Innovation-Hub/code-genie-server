import os
import requests

def test_basic_question_generation():
    server_url = os.getenv("SERVER_URL")
    topic = 'python'
    url = f"{server_url}/question_four_answers?topic={topic}"
    response = requests.get(url)
    assert response.status_code == 200
    answer = response.json()
    print()
    assert "question" in answer
    assert "correct_answer" in answer
    assert "python" in answer["question"].lower()    
    wrong_answers = [ans for ans in answer["wrong_answers"]]
    assert len(wrong_answers) == 3
    print("Test passed!")

test_basic_question_generation()
