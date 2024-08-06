from fastapi import APIRouter, Form
from data_access_layer import users

router = APIRouter()

@router.post('/add-user-stats/')
async def add_user_stats(user_id: str = Form(...), question_id = Form(...),
                         topic: str = Form(...), difficulty: str = Form(...),
                         answer_correct: bool = Form(...)):

    response = users.add_user_stats(user_id, question_id, topic, difficulty,
                                    answer_correct)
    return response
