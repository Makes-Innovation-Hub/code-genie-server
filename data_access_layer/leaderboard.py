from data_access_layer.setup_mongodb import setup_mongodb
from pymongo.errors import PyMongoError


def add_user_points(user_id: str, points: int, topic: str, difficulty: str, client=None):
    try:
        collection = setup_mongodb(client, 'points')
        db_topic = collection.find_one({'topic': topic})

        if db_topic:
            if difficulty not in db_topic:
                db_topic[difficulty] = {user_id: points}
            else:
                if user_id in db_topic[difficulty]:
                    db_topic[difficulty][user_id] += points
                else:
                    db_topic[difficulty][user_id] = points
            collection.replace_one({'topic': topic}, db_topic)
        else:
            db_topic = {"topic": topic, difficulty: {user_id: points}}
            collection.insert_one(db_topic)

        if '_id' in db_topic:
            del db_topic['_id']

        return db_topic

    except PyMongoError as e:
        print(f"Database error: {str(e)}")
        raise PyMongoError(f"Database error: {str(e)}")

    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise Exception(f"Unexpected error: {str(e)}")


def check_user_points_existence(data, client=None):
    collection = setup_mongodb(client, 'points')
    db_topic = collection.find_one({'topic': data['topic']})

    if not db_topic or data['difficulty'] not in db_topic or data['user_id'] not in db_topic[data['difficulty']]:
        return False
    previous_points = db_topic[data['difficulty']][data['user_id']] - data['points']
    if previous_points < 0:
        return False
    return True


def restore_db(data, client=None):
    collection = setup_mongodb(client, 'points')
    db_topic = collection.find_one({'topic': data['topic']})
    previous_points = db_topic[data['difficulty']][data['user_id']] - data['points']
    if previous_points == 0:
        del db_topic[data['difficulty']][data['user_id']]

        if not db_topic[data['difficulty']]:
            del db_topic[data['difficulty']]
        if len(db_topic) == 1:
            collection.delete_one({'topic': data['topic']})
            return True
    else:
        db_topic[data['difficulty']][data['user_id']] = previous_points

    collection.replace_one({'topic': data['topic']}, db_topic)
    return True


def get_user_points(data, client=None):
    collection = setup_mongodb(client, 'points')
    db_topic = collection.find_one({'topic': data['topic']})
    return db_topic[data['difficulty']][data['user_id']]
