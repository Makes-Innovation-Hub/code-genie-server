import random
from pymongo import MongoClient
from db.connection_credentials import mongodb_url

client = MongoClient(mongodb_url)
database = client['telegram_bot_data']
collection = database['tests']

def test_store_in_db():
    random_number = random.randint(1, 1000)
    if not check_exists_in_db(number=random_number):
        collection.insert_one({'random_number': random_number})
    return random_number

def check_exists_in_db(number: int):
    return collection.find_one({'random_number': number})

def delete_number_from_db(number: int):
    if check_exists_in_db(number=number):
        collection.delete_one({'random_number': number})
        return True
    return False
