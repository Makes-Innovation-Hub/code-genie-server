import random
from globals.CONSTANTS import ALLOWED_TOPICS
from globals import globals as gb

def store_num_in_db():
    mongo_client = gb.mongo_client
    if mongo_client:
        db = mongo_client["test_db"]
        collection = db["test"]
        random_number = random.randint(1, 1000)
        if not check_exists_in_db(number=random_number):
            collection.insert_one({'random_number': random_number})
        return random_number
    else:
        raise ValueError("mongo db client was not found")

def check_exists_in_db(number: int):
    mongo_client = gb.mongo_client
    if mongo_client:
        db = mongo_client["test_db"]
        collection = db["test"]
        return collection.find_one({'random_number': number})
    else:
        raise ValueError("mongo db client is not set up")

def delete_number_from_db(number: int):
    try:
        mongo_client = gb.mongo_client
        if mongo_client:
            db = mongo_client["test_db"]
            collection = db["test"]
            if check_exists_in_db(number=number):
                collection.delete_one({'random_number': number})
                return True
            return False
    except Exception as e:
        print(e)
        return e

def check_and_add_allowed_topics():
    mongo_client = gb.mongo_client
    if mongo_client:
        db = mongo_client["telegram_bot_data"]
        collection = db['topics']
        
        existing_topics = {doc['name'] for doc in collection.find()}

        missing_topics = ALLOWED_TOPICS - existing_topics

    if missing_topics:
        collection.insert_many([{"name": topic} for topic in missing_topics])
        print(f"Inserted missing topics: {missing_topics}")
    else:
        print("All allowed topics are present.")

        mongo_client.close()