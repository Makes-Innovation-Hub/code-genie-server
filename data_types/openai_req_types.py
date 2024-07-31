from pydantic import BaseModel,Literal

class GenQuestionBody(BaseModel):
    topic: str
    difficulty: Literal["easy","medium","hard","very hard"] | None