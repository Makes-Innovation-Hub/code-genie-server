import os
import requests
from data_access_layer.questions_db_functions import check_question_existence_and_delete, store_data
from globals import globals
from data_access_layer.topics_db_functions import *

def test_store_data():
    data = {
        'question': 'Are you mad?',
        'topic': 'general',
        'answer': 'No',
        'explanation': 'I am happy',
        'difficulty': 'easy',
        'user_name': 'basil',
        'user_id': '12'
    }

    response = store_data(data['question'], data['answer'], data['explanation'],
                          data['difficulty'], data['user_name'], data['user_id'], data['topic'], globals.mongo_client)
    # Check response pattern
    assert f"Question: '{data['question']}'." in response
    assert f"{data['user_name']} of id {data['user_id']}" in response
    assert f"answer: '{data['answer']}'." in response
    assert f"Explanation: '{data['explanation']}'" in response
    # Check if the question was added to the database and then delete it
    assert check_question_existence_and_delete(data=data, client=globals.mongo_client)


def test_load_topics_success():
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    url = f"{server_url}/question/topics/"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(isinstance(topic, str) for topic in response.json())


def test_add_topic():
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    url = f"{server_url}/question/topics?topic=Java"
    response = requests.post(url)
    assert response.status_code == 200
    assert response.json() == "Java added successfully"
    assert check_topic_and_delete("Java")

def test_add_exists_topic():
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    url = f"{server_url}/question/topics?topic=python"
    response = requests.post(url)
    assert response.status_code == 409
    assert response.json()['detail'] == 'python is already in the list topics'

