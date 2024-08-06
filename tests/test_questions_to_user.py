from data_access_layer.questions_to_user import check_question_existence_and_delete, store_data

def test_store_data():

    data = {
        'question': 'Are you mad?',
        'answer': 'No',
        'explanation': 'I am happy',
        'difficulty': 'easy',
        'user_name': 'basil',
        'user_id': '12'
    }

    response = store_data(data['question'], data['answer'], data['explanation'],
                          data['difficulty'], data['user_name'], data['user_id'])
    # Check response pattern
    assert f"Question: '{data['question']}'." in response
    assert f"{data['user_name']} of id {data['user_id']}" in response
    assert f"answer: '{data['answer']}'." in response
    assert f"Explanation: '{data['explanation']}'" in response
    # Check if the question was added to the database and then delete it
    assert check_question_existence_and_delete(data=data)
