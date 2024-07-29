import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))

def get_question_and_answer(topic):
    prompt = f"I need you to generate a new  technical question and answer for a computer science graduate about: {topic}"
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150, 
            temperature=0.7,
        )
        generated_text = response.choices[0].message.content.strip()
        lines = generated_text.split('\n\n')
        question = None
        answer = None
        
        for line in lines:
            if line.lower().startswith("question:"):
                question = line[len("Question:"):].strip()
            elif line.lower().startswith("answer:"):
                answer = line[len("Answer:"):].strip()

        return {"question": question, "answer": answer}
    except Exception as e:
        return {"error": str(e)}
    


def get_chat_completion(prompt: str) -> str:
    try: 
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