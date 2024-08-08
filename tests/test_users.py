from data_access_layer.users import *
from globals import globals


def test_add_user_stats():
    data = {
        'user_id': '10000',
        'question_id': '1',
        'topic': 'Animals',
        'difficulty': 'hard',
        'answer_correct': True,
        'score': 8,
        'answer': 'my answer'
    }

    response = add_user_stats(user_id=data['user_id'], question_id=data['question_id'], topic=data['topic'],
                              difficulty=data['difficulty'],
                              answer_correct=data['answer_correct'], score=data['score'], answer=data['answer'],
                              client=globals.mongo_client)
    response = str(response)
    assert 'user_id' in response
    assert 'questions' in response
    assert data['question_id'] in response
    assert 'topics' in response
    assert data['topic'] in response
    assert data['difficulty'] in response
    assert 'questions_answered' in response
    assert 'questions_answered_correctly' in response
    assert data['answer'] in response
    assert str(data['score']) in response
    assert check_user_existence_and_delete(data=data, client=globals.mongo_client)
