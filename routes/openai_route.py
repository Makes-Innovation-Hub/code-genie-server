from fastapi import APIRouter, Request, Response
from logging_pac.logging_setup import logger, RequestIDMiddleware,log_request_handling
from services.openai_service import get_chat_completion, get_question_and_answer
from data_types.openai_req_types import GenQuestionBody as GenBody

router = APIRouter()

@router.post('/basic')
async def gen_basic_question(body:GenBody, request: Request):
    try:
        answer = get_question_and_answer(topic)
        request_id = request.state.request_id
        log_request_handling(request_id, "this is test from the basic question")
    except Exception as e:
        print(e)
        response.status_code = 400
        return e
      
@router.post('/generate')
async def gen_question(body:GenBody, response: Response):
    topic = body.topic
    difficulty = body.difficulty
    answers_num = body.answers_num
    try:
        answer = get_question_and_answer(topic,difficulty,answers_num)
        log_request_handling(request_id, "this is test from the basic question")
        return answer
    except Exception as e:
        print(e)
        response.status_code = 400
        return e