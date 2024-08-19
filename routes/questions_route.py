from fastapi import APIRouter, Form
from data_access_layer import questions_db_functions
from data_access_layer.topics_db_functions import get_topics
from pymongo import errors

router = APIRouter()


@router.post('/store-data/')
async def store_data(question: str = Form(...), answer: str = Form(...), topic: str = Form(...),
                     explanation: str = Form(...), difficulty: str = Form(...),
                     user_name: str = Form(...), user_id: str = Form(...)):
    response = questions_db_functions.store_data(question=question, topic=topic, answer=answer, explanation=explanation,
                                            difficulty=difficulty, user_name=user_name, user_id=user_id)

    return response


@router.get('/topics/')
async def load_topics():
    try:
        topics = get_topics()
        return topics
    except errors.ConnectionFailure as c:
        raise f"Connection error occurred: {c}"
    except Exception as e:
        raise f"An unexpected error occurred: {e}"
