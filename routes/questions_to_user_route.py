from fastapi import APIRouter, Form
from data_access_layer import questions_to_user

router = APIRouter()


@router.post('/store-data/')
async def store_data(question: str = Form(...), answer: str = Form(...),
                     explanation: str = Form(...), difficulty: str = Form(...),
                     user_name: str = Form(...), user_id: str = Form(...)):
    response = questions_to_user.store_data(question=question, answer=answer, explanation=explanation,
                                            difficulty=difficulty, user_name=user_name, user_id=user_id)

    return response


@router.post('/generate-question/')
async def generate_question(topic: str = Form(...)):
    response = questions_to_user.generate_question(topic=topic)
    return response

@router.post('/generate-question-with-multiple-answers/')
async def generate_question_with_multiple_answers(topic: str = Form(...)):
    response = questions_to_user.generate_question_with_multiple_answers(topic=topic)
    return response
