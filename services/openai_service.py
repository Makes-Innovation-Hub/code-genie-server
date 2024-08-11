import os
from openai import OpenAI
import json
from globals.CONSTANTS import GEN_QUESTION_JSON_FORMAT as json_format


def get_question_and_answer(topic, difficulty, answers_num) -> dict:
    prompt = generate_question_prompt(topic,difficulty,answers_num)
    try:
        generated_text = get_chat_completion(prompt)
        return process_chat_response(generated_text,difficulty)
    except Exception as e:
        print("error in gen question and answer",e)
        raise e

def get_chat_completion(prompt: str) -> str:
    try:
        client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))
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
        print('e: ', e)
        raise e

def generate_question_prompt(topic, difficulty = None, answers_num= None):
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

def process_chat_response(chat_response,difficulty):
    try:
        json_response = json.loads(chat_response)
        if difficulty:
            json_response["difficulty"] = difficulty
        return json_response
    except Exception as e:
        print(f"error in processing chat response: ",e)
        raise e