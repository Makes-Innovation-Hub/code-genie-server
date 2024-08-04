import os
import requests
from data_access_layer.questions_to_user import check_question_existence_and_delete

def test_store_data():
    data = {
        'question': 'Are you mad?',
        'answer': 'No',
        'explanation': 'I am happy',
        'difficulty': 'easy',
        'user_name': 'basil',
        'user_id': '12'
    }
    # server_url = 'http://localhost:8002'
    server_url = os.getenv('SERVER_URL')
    response = requests.post(f'{server_url}/questions-to-user/store-data/', data=data)
    assert response.status_code == 200
    # Check if the question was added to the database and then delete it
    assert check_question_existence_and_delete(data=data)
