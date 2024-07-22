import random
from pymongo import MongoClient
from db.connection_credentials import mongodb_url


class BasicDbFunctions:
    def __init__(self):
        client = MongoClient(mongodb_url)
        database = client['telegram_bot_data']
        self.collection = database['tests']

    def test(self):
        random_number = random.randint(1, 1000)
        self.collection.insert_one({'random_number': random_number})
        return random_number
