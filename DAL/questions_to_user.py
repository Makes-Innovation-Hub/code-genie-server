from pymongo import MongoClient
from db.connection_credentials import mongodb_url


class QuestionsToUser:
    def __init__(self):
        client = MongoClient(mongodb_url)
        database = client['telegram_bot_data']
        self.collection = database['Questions']

    def store_data(self, question: str, answer: str, explanation: str, difficulty: str, user_name: str, user_id: str):
        db_question = self.collection.find_one({'question': question})

        if db_question:
            db_question['answers'][user_id] = answer
            db_question['explanations'][user_id] = explanation
            db_question['users_details'][user_id] = user_name

            self.collection.replace_one({'question': question}, db_question)

        else:
            data = {
                'question': question,
                'answers': {user_id: answer},
                'explanations': {user_id: explanation},
                'difficulty': difficulty,
                'users_details': {user_id: user_name}
            }

            self.collection.insert_one(data)

        return f"Question: '{question}'. {user_name} of id {user_id} answer: '{answer}'. Explanation: '{explanation}'"
