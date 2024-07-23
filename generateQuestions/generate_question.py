import os
import openai
from dotenv import load_dotenv
load_dotenv()
# this function sends a request to openai api to generate a question about any topic (it takes the topic as a parameter and returns the question and the answer as a dict)
def get_question_and_answer(topic):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    prompt = f"I need you to generate a new  technical question and answer for a computer science graduate about: {topic}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150, 
            temperature=0.7,
        )
        generated_text = response['choices'][0]['message']['content'].strip()
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
    

