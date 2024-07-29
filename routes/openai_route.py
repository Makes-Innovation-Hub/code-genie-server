from fastapi import APIRouter
from services.openai_service import get_chat_completion, get_question_and_answer
from data_types.openai_req_types import GenQuestionBody as GenBody

router = APIRouter()

@router.post('/basic')
async def gen_basic_question(body:GenBody):
    topic = body.topic
    try:
        answer = get_question_and_answer(topic)
        return answer
    except Exception as e:
        print(e)
        return e


@router.get('/test')
async def get_basic_chat():
    try:
        answer = get_chat_completion("return just the word: hello with no quotation marks")
        return answer
    except Exception as e:
        print(e)
        return e
