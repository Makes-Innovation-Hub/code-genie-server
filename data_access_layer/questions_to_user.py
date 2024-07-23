from pymongo import MongoClient
from db.connection_credentials import mongodb_url
from generate_questions.generate_question import *
from generate_questions.generate_question_4_answers import get_question_and_answers

client = MongoClient(mongodb_url)
database = client['telegram_bot_data']

def store_data(question: str, answer: str, explanation: str, difficulty: str, user_name: str, user_id: str):
    collection = database['Questions']

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

def generate_question(topic: str):
    collection = database['GeneratedQuestions']
    response = get_question_and_answer(topic=topic)
    question = response['question']

    while not question:
        response = get_question_and_answer(topic=topic)
        question = response['question']

    db_question = collection.find_one({'question': question})

    while db_question:
        response = get_question_and_answer(topic=topic)
        question = response['question']
        db_question = collection.find_one({'question': question})

    collection.insert_one(response)
    # The insert_one function adds _id field to the response variable which is not serializable by FastAPI
    del response['_id']
    return response

def generate_question_with_multiple_answers(topic: str):
    collection = database['GeneratedMultipleQuestions']
    response = get_question_and_answers(topic=topic)
    question = response['question']

    while not question:
        response = get_question_and_answers(topic=topic)
        question = response['question']

    db_question = collection.find_one({'question': question})

    while db_question:
        response = get_question_and_answers(topic=topic)
        question = response['question']
        db_question = collection.find_one({'question': question})
        if db_question:
            if not db_question['question']:
                db_question = True

    collection.insert_one(response)
    # The insert_one function adds _id field to the response variable which is not serializable by FastAPI
    del response['_id']
    return response
