import random
from pymongo import MongoClient
from db.connection_credentials import mongodb_url

client = MongoClient(mongodb_url)
database = client['telegram_bot_data']
collection = database['tests']

def test_store_in_mongodb():
    random_number = random.randint(1, 1000)
    collection.insert_one({'random_number': random_number})
    return random_number
