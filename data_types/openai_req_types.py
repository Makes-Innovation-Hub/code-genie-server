from pydantic import BaseModel
from typing import Literal


class GenQuestionBody(BaseModel):
    topic: str
    difficulty: None | Literal["easy", "medium", "hard", "very hard"] = None
    answers_num: int | None = None


class QARequest(BaseModel):
    user_id: str
    question_id: str
    question: str | None = None
    answer: str
