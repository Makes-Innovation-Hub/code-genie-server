from fastapi import APIRouter, Form
from data_access_layer import basic_db_functions,questions_to_user
router = APIRouter()

@router.get('/test')
async def store_rand_num_in_db():
    try:
        stored_number = basic_db_functions.store_num_in_db()
        print(f'{stored_number} was stored successfully')
        return {"stored_number":stored_number}
    except Exception as e:
        raise e


@router.post('/store-data/')
async def store_data(question: str = Form(...), answer: str = Form(...),
                     explanation: str = Form(...), difficulty: str = Form(...),
                     user_name: str = Form(...), user_id: str = Form(...)):

    response = questions_to_user.store_data(question=question, answer=answer, explanation=explanation,
                                            difficulty=difficulty, user_name=user_name, user_id=user_id)

    return response
