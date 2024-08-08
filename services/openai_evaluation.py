import ast

from globals.CONSTANTS import EVALUATE_QUESTION_JSON_FORMAT
from services.openai_service import get_chat_completion


def evaluate_answer(question: str, answer: str) -> dict:
    prompt = f""" You are an expert evaluator. Evaluate the following answer to the question and provide a short 
    explanation followed by a score between 0 and 10, with 0 being the lowest ,if the answer is empty evaluate 0.\n
    Question: {question}
    Answer: {answer}
    Provide your evaluation in the following format {EVALUATE_QUESTION_JSON_FORMAT}:
    """
    evaluation = get_chat_completion(prompt)
    evaluation = ast.literal_eval(evaluation)
    evaluation["Score"] = int(evaluation["Score"])
    return evaluation
