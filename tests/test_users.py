from data_access_layer.users_db_functions import *
from globals import globals


def test_add_user_stats():
    data = {
        'user_id': '10000',
        'question_text': 'Which class of animals are newts members of?',
        'topic': 'Animals',
        'difficulty': 'easy',
        'is_correct': True,
        'score': 8,
        'answer': 'my answer'
    }

    response = add_user_stats(data['user_id'], data['question_text'],data['score'],data['answer'], data['topic'], data['difficulty'],
                              data['is_correct'])
    response = str(response)
    assert 'user_id' in response
    assert 'questions' in response
    assert data['question_text'] in response
    assert 'topics' in response
    assert data['topic'] in response
    assert data['difficulty'] in response
    assert 'questions_answered' in response
    assert 'questions_answered_correctly' in response
    assert data['answer'] in response
    assert str(data['score']) in response
    assert check_user_existence_and_delete(data=data)
