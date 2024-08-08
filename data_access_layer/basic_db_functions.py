import random
from fastapi import Request
from logging_packages.logging_setup import logger, RequestIDMiddleware,log_request_handling
from globals import globals as gb

def store_num_in_db(request: Request):
    request_id = request.state.request_id
    mongo_client = gb.mongo_client
    if mongo_client:
        db = mongo_client["test_db"]
        collection = db["test"]
        log_request_handling(request_id, 'connected to mongoDB successfuly')
        random_number = random.randint(1, 1000)
        if not check_exists_in_db(number=random_number, request= request):
            collection.insert_one({'random_number': random_number})
        return random_number
    else:
        log_request_handling(request_id, 'mongo db client was not found')
        raise ValueError("mongo db client was not found")

def check_exists_in_db(number: int, request: Request):
    request_id = request.state.request_id
    mongo_client = gb.mongo_client
    if mongo_client:
        db = mongo_client["test_db"]
        collection = db["test"]
        log_request_handling(request_id, 'number found in mongo db')
        return collection.find_one({'random_number': number})
    else:
        log_request_handling(request_id, 'mongo db client is not set up')
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
