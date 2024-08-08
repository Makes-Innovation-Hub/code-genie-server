import os
from openai import OpenAI
from fastapi import APIRouter, Request, Response
import json
from logging_packages.logging_setup import logger, RequestIDMiddleware,log_request_handling
import dotenv
from globals.CONSTANTS import GEN_QUESTION_JSON_FORMAT as json_format

openai_key = os.getenv("OPENAI_API_KEY")
if openai_key is None:
    raise ValueError("Could not load openai key correctly")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_question_and_answer(topic, difficulty, answers_num, request: Request) -> dict:
    request_id = request.state.request_id
    prompt = generate_question_prompt(topic,request,difficulty, answers_num)
    log_request_handling(request_id, "data sent to generate_question_prompt to get a prompt.")
    try:
        generated_text = get_chat_completion(prompt, request)
        log_request_handling(request_id, "prompt sent, waiting for response")
        return process_chat_response(generated_text,difficulty, request)
    except Exception as e:
        log_request_handling(request_id, "error in gen question and answer{e}")
        raise e

def get_chat_completion(prompt: str, request: Request) -> str:
    request_id = request.state.request_id
    log_request_handling(request_id, "got the prompt in get_chat_completion.")
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            temperature=0.7,
        )
        generated_text = response.choices[0].message.content.strip()
        return generated_text
    except Exception as e:
        log_request_handling(request_id, e)        
        raise e

def generate_question_prompt(topic, request: Request, difficulty = None, answers_num= None):
    request_id = request.state.request_id
    log_request_handling(request_id, "generating a prompt in generate_question_prompt.")
    prompt = (f"I need you to generate a new single technical question for a"
              f"computer science graduate about: {topic}. response with this EXACT json format: "
              f"{json_format}. The values in the JSON are explanations regarding the "
              f"values and the structure of each field.")
    if answers_num and isinstance(answers_num, int) and answers_num>1:
        prompt += (f"Generate 1 correct answer and {answers_num -1} wrong ones. "
                   f"Make SURE that the answers list includes {answers_num} values "
                   f"Make SURE that the explanations list includes {answers_num} values. ")
    else:
        prompt += """Please generate a single answer and a single explanation.  
                    Make SURE to put the answer and the explanation inside the
                    correct location within the json format. """
    prompt += """Don't include any pleasantries or any other text that is not
               specified in the json format I have given you. MAKE SURE to return Keys and 
               values wrapped by double quotes and NOT single quotes. MAKE SURE 
               that your response is a valid JSON"""
    if difficulty:
        prompt += f'Please make sure that the difficulty of the question is {difficulty}. '
    return prompt

def process_chat_response(chat_response,difficulty, request: Request):
    request_id = request.state.request_id
    try:
        json_response = json.loads(chat_response)
        if difficulty:
            json_response["difficulty"] = difficulty
        return json_response
    except Exception as e:
        log_request_handling(request_id, f"error in processing chat response: {e}")
        raise e