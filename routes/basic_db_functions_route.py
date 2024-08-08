from fastapi import APIRouter, Request
from data_access_layer import basic_db_functions
from logging_packages.logging_setup import logger, RequestIDMiddleware,log_request_handling


router = APIRouter()

@router.get('/test')
async def store_rand_num_in_db( request: Request):
    try:
        request_id = request.state.request_id
        stored_number = basic_db_functions.store_num_in_db(request)
        log_request_handling(request_id, f'{stored_number} was stored successfully')
        return {"stored_number":stored_number}
    except Exception as e:
        log_request_handling(request_id, e)
        raise e
