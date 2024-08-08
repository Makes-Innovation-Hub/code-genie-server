from data_access_layer.setup_mongodb import setup_mongodb
from pymongo.errors import PyMongoError


def add_user_stats(user_id: str, question_text: str, score: int, answer: str, topic: str, difficulty: str ,
                   answer_correct: bool,
                   client):
    try:
        collection = setup_mongodb(client, 'users')
        db_user = collection.find_one({'user_id': user_id})
        question_score = {'question_text': question_text, 'score': score, 'answer': answer}
        if db_user:
            db_user['questions'].append(question_score)
            if topic not in db_user['topics'].keys():
                db_user['topics'][topic] = {}
            if difficulty not in db_user['topics'][topic].keys():
                db_user['topics'][topic][difficulty] = {'questions_answered': 0,
                                                        'questions_answered_correctly': 0}
            if answer_correct:
                db_user['topics'][topic][difficulty]['questions_answered_correctly'] += 1
            db_user['topics'][topic][difficulty]['questions_answered'] += 1
            collection.replace_one({'user_id': user_id}, db_user)
        else:
            if answer_correct:
                db_user = {
                    'user_id': user_id,
                    'questions': [question_score],
                    'topics': {topic: {difficulty: {'questions_answered': 1,
                                                    'questions_answered_correctly': 1}}}
                }
            else:
                db_user = {
                    'user_id': user_id,
                    'questions': [question_score],
                    'topics': {topic: {difficulty: {'questions_answered': 1,
                                                    'questions_answered_correctly': 0}}}
                }
            collection.insert_one(db_user)

        del db_user['_id']
        return db_user
    except PyMongoError as e:
        print(f"Database error: {str(e)}")
        raise PyMongoError(f"Database error: {str(e)}")  # Raise the caught PyMongoError with the error message
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise Exception(f"Unexpected error: {str(e)}")

def check_user_existence_and_delete(data, client):
    collection = setup_mongodb(client, 'users')
    db_user = collection.find_one({'user_id': data['user_id']})

    if db_user:
        collection.delete_one({'user_id': data['user_id']})
        return True

    return False
