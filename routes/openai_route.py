from fastapi import APIRouter, Response
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
async def gen_question(body: QARequest, response: Response):
    try:
        question = body.question
        answer = body.answer
        evaluation_score = evaluate_answer(question=question, answer=answer)
        return evaluation_score
    except Exception as e:
        print(e)
        response.status_code == 400
        return e
