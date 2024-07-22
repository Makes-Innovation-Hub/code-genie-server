import random

from pymongo import MongoClient
from db.connection_credentials import mongodb_url


class QuestionsToUser:
    def __init__(self):
        client = MongoClient(mongodb_url)
        self.database = client['telegram_bot_data']

    def store_data(self, question: str, answer: str, explanation: str, difficulty: str, user_name: str, user_id: str):
        collection = self.database['Questions']

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

    def generate_question(self):
        collection = self.database['GeneratedQuestions']

        questions = [
            "What is your favorite color?",
            "How old are you?",
            "Where do you live?",
            "What is your hobby?",
            "What is your favorite food?",
            "What is your favorite movie?",
            "What is your dream job?",
            "What is your favorite book?",
            "What is your favorite animal?",
            "What is your favorite season?"
        ]
        question = random.choice(questions)

        db_question = collection.find_one({'question': question})

        if db_question:
            return None

        collection.insert_one({'question': question})
        return question
