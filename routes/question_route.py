from fastapi import APIRouter, Response
from services.openai_service import get_chat_completion, get_question_and_answer
from data_types.openai_req_types import GenQuestionBody as GenBody

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
async def gen_question(body: GenBody, response: Response):
    pass
