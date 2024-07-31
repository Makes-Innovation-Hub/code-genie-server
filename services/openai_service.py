import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai_key = os.environ.get("OPENAI_KEY")
if openai_key is None:
    raise ValueError("Could not load openai key correctly")
client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))

def get_question_and_answer(topic, difficulty) -> dict:
    prompt = (f"I need you to generate a new  technical question and answer for a"
              f"computer science graduate about: {topic}. return just the question"
              f"starting with 'Question: ' and after the question start the answer"
              f"with 'Answer: '. Don't include any pleasantries or any other text"
              f"before the question or after the answer. add an empty line"
              f"between the question and the answer.")
    if difficulty:
        prompt += f',please make sure that the difficulty of the question is {difficulty}'
    try:
        generated_text = get_chat_completion(prompt)
        lines = generated_text.split('\n\n')
        question = None
        answer = None
        for line in lines:
            if line.lower().startswith("question:"):
                question = line[len("Question:"):].strip()
            elif line.lower().startswith("answer:"):
                answer = line[len("Answer:"):].strip()
        final_answer = {"question": question, "answer": answer}
        if difficulty:
            final_answer["difficulty"] = difficulty

        return final_answer
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
            max_tokens=150,
            temperature=0.7,
        )
        generated_text = response.choices[0].message.content.strip()

        return generated_text
    except Exception as e:
        print('e: ', e)
        raise e
