from globals.globals import mongo_client
from pymongo import MongoClient

# client = MongoClient('mongodb://localhost:27017/')
# database = client['telegram_bot_data']
# collection = database['Questions']

database = mongo_client['telegram_bot_data']
collection = database['Questions']

def store_data(question: str, answer: str, explanation: str, difficulty: str, user_name: str, user_id: str):
    db_question = collection.find_one({'question': question})

    if db_question:
        db_question['answers'][user_id] = answer
        db_question['explanations'][user_id] = explanation
        db_question['users_details'][user_id] = user_name

        collection.replace_one({'question': question}, db_question)

    else:
        data = {
            'question': question,
            'answers': {user_id: answer},
            'explanations': {user_id: explanation},
            'difficulty': difficulty,
            'users_details': {user_id: user_name}
        }

        collection.insert_one(data)

    return f"Question: '{question}'. {user_name} of id {user_id} answer: '{answer}'. Explanation: '{explanation}'"

def check_question_existence_and_delete(data):
    db_question = collection.find_one({'question': data['question'], 'difficulty': data['difficulty']})

    if db_question:
        collection.delete_one(data)
        return True

    return False
