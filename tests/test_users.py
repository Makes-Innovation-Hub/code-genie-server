from data_access_layer.users import *

def test_add_user_stats():
    data = {
        'user_id': '10000',
        'question_id': '1',
        'topic': 'Animals',
        'difficulty': 'hard',
        'answer_correct': True,
    }

    response = add_user_stats(data['user_id'], data['question_id'], data['topic'], data['difficulty'],
                              data['answer_correct'])
    response = str(response)
    assert 'user_id' in response
    assert 'questions_id' in response
    assert 'topics' in response
    assert data['topic'] in response
    assert data['difficulty'] in response
    assert 'questions_answered' in response
    assert 'questions_answered_correctly' in response
    assert check_user_existence_and_delete(data=data)
