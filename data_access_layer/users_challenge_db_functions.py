from fastapi import HTTPException
from data_access_layer.setup_mongodb import setup_mongodb

def store_username(username: str, client=None):
    collection = setup_mongodb(client, 'users_challenge')
    db_username = collection.find_one({'username': username})

    if db_username:
        raise HTTPException(status_code=409, detail='Username already exists')

    username_data = {
        'username': username,
        'available': True
    }
    collection.insert_one(username_data)
    del username_data['_id']

    return username_data

def fetch_username_for_challenge(client=None, username=None):
    collection = setup_mongodb(client, 'users_challenge')
    if username:
        db_username = collection.find_one({'username': username, 'available': True})
    else:
        db_username = collection.find_one({'available': True})

    if not db_username:
        raise HTTPException(status_code=404, detail='No available username found')

    db_username['available'] = False
    collection.replace_one({'username': db_username['username']}, db_username)

    return db_username['username']

def check_and_delete_username(username: str, client=None):
    collection = setup_mongodb(client, 'users_challenge')
    db_username = collection.find_one({'username': username})

    if not db_username:
        return False

    collection.delete_one({'username': username})
    return True
