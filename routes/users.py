from fastapi import APIRouter, Form
from data_access_layer import users
from data_access_layer.users_challenge_db_functions import store_username

router = APIRouter()


@router.post('/add-user-stats/')
async def add_user_stats(user_id: str = Form(...), question_text: str = Form(...),
                         topic: str = Form(...), difficulty: str = Form(...),
                         answer_correct: bool = Form(...), score: int = Form(...),answer:str = Form(...)):
    response = users.add_user_stats(user_id, question_text, score,answer, topic, difficulty,
                                    answer_correct)
    return response


@router.post('/add-username-challenge')
async def add_username(username: str):
    try:
        response = store_username(username=username)
        return response
    except Exception as e:
        raise e