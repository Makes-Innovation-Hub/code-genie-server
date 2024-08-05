from pymongo import MongoClient
from globals import globals
import os
from urllib.parse import quote_plus


def set_mongo_client():
    try:
        mongodb_username = quote_plus(os.getenv('MONGODB_USERNAME'))
        mongodb_password = quote_plus(os.getenv('MONGODB_PASSWORD'))
        mongodb_host = os.getenv('MONGODB_HOST')
        if mongodb_username and mongodb_password and mongodb_host:
            mongodb_url = f'mongodb+srv://{mongodb_username}:{mongodb_password}@{mongodb_host}'
            client = MongoClient(mongodb_url)
            globals.mongo_client = client
            return
        else:
            raise KeyError("one or more of mongo env var keys is not found")
    except Exception as e:
        print(f"error in mongo initial setup: {e}")
        raise e
    