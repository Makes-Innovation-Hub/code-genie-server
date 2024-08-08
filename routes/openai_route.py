from fastapi import APIRouter, Response
from globals import globals
from data_access_layer import users
from services.openai_service import get_question_and_answer,evaluate_answer
from data_types.openai_req_types import GenQuestionBody as GenBody, QARequest
from pymongo.errors import PyMongoError

router = APIRouter()


@router.post('/generate')
async def gen_question(body: GenBody, response: Response):
    topic = body.topic
    difficulty = body.difficulty
    answers_num = body.answers_num
    try:
        answer = get_question_and_answer(topic, difficulty, answers_num)
        return answer
    except Exception as e:
        print(e)
        response.status_code = 400
        return e



@router.post('/evaluate')
async def evaluate_question(body: QARequest, response: Response):
    try:
        user_id = body.user_id
        question_text = body.question_text
        topic = body.topic
        difficulty = body.difficulty
        answer = body.answer
        evaluation_score = evaluate_answer(question=question_text, answer=answer)
        users.add_user_stats(user_id=user_id, question_text=question_text, answer=answer, topic=topic,
                             difficulty=difficulty,
                             score=evaluation_score["Score"], answer_correct=(evaluation_score["Score"] >= 5),
                             client=globals.mongo_client)
        return evaluation_score
    except PyMongoError as e:
        print(f"Database error: {str(e)}")
        response.status_code = 500
        return {"error": "A database error occurred. Please try again later."}

    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        response.status_code = 500
        return {"error": "An unexpected error occurred. Please try again later."}