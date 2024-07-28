from fastapi import FastAPI
from generateQuestions import generate_question_4_answers
app = FastAPI()


@app.get('/')
async def root():
    return 'Hello from FastAPI server'

# @app.get('/question_four_answers')
# async def get_question_four_answers(topic: str):
#     try:
#         answer = generate_question_4_answers.get_question_and_answers(topic)
#         print(answer)
#         return answer
#     except Exception as e:
#         print(e)
#         return e
