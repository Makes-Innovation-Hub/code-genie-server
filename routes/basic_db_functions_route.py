from fastapi import APIRouter
from DAL.basic_db_functions import BasicDbFunctions

router = APIRouter()


@router.get('/')
async def test():
    basic_db_functions = BasicDbFunctions()
    stored_number = basic_db_functions.test()

    return f'{stored_number} was stored successfully'
