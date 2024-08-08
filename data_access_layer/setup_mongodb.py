def setup_mongodb(client, collection_name: str):
    database = client['telegram_bot_data']
    collection = database[collection_name]
    return collection
