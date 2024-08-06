from fastapi import APIRouter
from data_access_layer import basic_db_functions

router = APIRouter()

@router.get('/test')
async def store_rand_num_in_db():
    try:
        stored_number = basic_db_functions.store_num_in_db()
        print(f'{stored_number} was stored successfully')
        return {"stored_number":stored_number}
    except Exception as e:
        raise e
