from pydantic import BaseModel
from typing import Literal
class GenQuestionBody(BaseModel):
    topic: str
    difficulty: None | Literal["easy","medium","hard","very hard"] = None
    answers_num: int | None = None