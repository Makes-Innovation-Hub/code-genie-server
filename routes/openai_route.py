from fastapi import APIRouter, Request, Response
from logging_packages.logging_setup import logger, RequestIDMiddleware,log_request_handling
from services.openai_service import get_chat_completion, get_question_and_answer
from data_types.openai_req_types import GenQuestionBody as GenBody

router = APIRouter()

      
@router.post('/generate')
async def gen_question(body:GenBody, response: Response, request: Request):
    topic = body.topic
    difficulty = body.difficulty
    answers_num = body.answers_num
    request_id = request.state.request_id
    try:
        log_request_handling(request_id, "generating a new question.")
        answer = get_question_and_answer(topic,difficulty,answers_num, request)
        log_request_handling(request_id, "new question generated successfully.")
        return answer
    except Exception as e:
        log_request_handling(request_id, e)
        response.status_code = 400
        return e