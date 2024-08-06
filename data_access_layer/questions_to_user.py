from data_access_layer.setup_mongodb import setup_mongodb

def store_data(question: str, answer: str, explanation: str, difficulty: str, user_name: str, user_id: str,
               client=None):
    collection = setup_mongodb(client, 'Questions')
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


def check_question_existence_and_delete(data, client=None):
    collection = setup_mongodb(client, 'Questions')
    filter = {'question': data['question'], 'difficulty': data['difficulty']}
    db_question = collection.find_one(filter)

    if db_question:
        collection.delete_one(filter)
        return True

    return False
