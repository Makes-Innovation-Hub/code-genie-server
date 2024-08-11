from globals import globals

def setup_mongodb(client, collection_name: str):
    if client:
        database = client['telegram_bot_data']
        collection = database[collection_name]
    else:
        database = globals.mongo_client['telegram_bot_data']
        collection = database[collection_name]

    return collection
