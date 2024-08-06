import random

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
