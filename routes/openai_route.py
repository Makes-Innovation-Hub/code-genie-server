from fastapi import APIRouter, Response
from globals import globals
from data_access_layer import users
from data_access_layer.questions_to_user import get_question_info
from services.openai_evaluation import evaluate_answer
from services.openai_service import get_question_and_answer
from data_types.openai_req_types import GenQuestionBody as GenBody, QARequest

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
        question = body.question
        question_id = body.question_id
        answer = body.answer
        question_info = get_question_info(question_id, globals.mongo_client)
        if question_info:

            evaluation_score = evaluate_answer(question=question, answer=answer)
            users.add_user_stats(user_id=user_id, question_id=question_id, answer=answer,
                                 score=evaluation_score["Score"], answer_correct=(evaluation_score["Score"] >= 5))
            return evaluation_score
        else:
            print("question info not found ???????????????")
    except Exception as e:
        print(e)
        response.status_code = 400
        return e
