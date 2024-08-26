from data_access_layer.setup_mongodb import setup_mongodb
from globals.CONSTANTS import ALLOWED_TOPICS
from pymongo import errors


def check_and_add_allowed_topics():
    try:
        collection = setup_mongodb(client=None, collection_name='topics')
        existing_topics = {doc['name'] for doc in collection.find()}

        missing_topics = ALLOWED_TOPICS - existing_topics

        if missing_topics:
            collection.insert_many([{"name": topic} for topic in missing_topics])
            print(f"Inserted missing topics: {missing_topics}")
        else:
            print("All allowed topics are present.")

    except errors.ConnectionFailure as c:
        raise f"Connection error occurred: {c}"
    except errors.OperationFailure as o:
        raise f"Database operation failed: {o}"
    except Exception as e:
        raise f"An unexpected error occurred: {e}"


def get_topics():
    try:
        collection = setup_mongodb(client=None, collection_name='topics')
        topics = {doc['name'] for doc in collection.find()}
        return topics
    except errors.ConnectionFailure as c:
        raise f"Connection error occurred: {c}"
    except Exception as e:
        raise f"An unexpected error occurred: {e}"
