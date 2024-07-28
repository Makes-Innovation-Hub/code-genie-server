from fastapi import APIRouter
from services.openai_service import get_chat_completion
router = APIRouter()

@router.get('/test')
async def get_basic_chat():
    try:
        answer = get_chat_completion("return just the word: hello with no quotation marks")
        return answer
    except Exception as e:
        print(e)
        return e
