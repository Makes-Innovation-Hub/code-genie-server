from pydantic import BaseModel

class GenQuestionBody(BaseModel):
    topic: str