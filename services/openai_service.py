import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def get_question_and_answer(topic='', difficulty=''):
    prompt = f"I need you to generate a new  technical question and answer for a computer science graduate "
    if topic:
        prompt += f'about: {topic}'
    if difficulty:
        prompt += f',please make sure that the difficulty of the question is {difficulty}'
    try:
        generated_text = get_chat_completion(prompt)
        lines = generated_text.split('\n\n')
        question = lines[0].split(':')[1].strip()
        answer = lines[1].split(':')[1].strip()

        final_answer = {"question": question, "answer": answer}
        if difficulty:
            final_answer["difficulty"] = difficulty

        return final_answer
    except Exception as e:
        return {"error": str(e)}


def get_chat_completion(prompt: str) -> str:
    try:

        client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        generated_text = response.choices[0].message.content.strip()

        return generated_text
    except Exception as e:
        print('e: ', e)
        return e


