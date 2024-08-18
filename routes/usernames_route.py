from fastapi import APIRouter
from data_access_layer import usernames_dal

router = APIRouter()

@router.post('/')
async def store_username(username: str):
    try:
        response = usernames_dal.store_username(username=username)
        return response
    except Exception as e:
        raise e

@router.get('/')
async def fetch_username_for_challenge():
    try:
        response = usernames_dal.fetch_username_for_challenge()
        return response
    except Exception as e:
        raise e
