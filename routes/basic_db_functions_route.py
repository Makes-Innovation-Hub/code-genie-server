from fastapi import APIRouter
from data_access_layer import basic_db_functions

router = APIRouter()

@router.get('/')
async def test_store_in_db():
    stored_number = basic_db_functions.test_store_in_db()
    return f'{stored_number} was stored successfully'
