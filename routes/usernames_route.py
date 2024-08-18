from fastapi import APIRouter
from data_access_layer.usernames_dal import store_username

router = APIRouter()

@router.post('/')
async def add_username(username: str):
    try:
        response = store_username(username=username)
        return response
    except Exception as e:
        raise e
