import os
import openai
from dotenv import load_dotenv
load_dotenv()

def get_chat_completion(prompt: str) -> str:
    openai.api_key = os.getenv('OPENAI_API_KEY')
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
        return generated_text
    except Exception as e:
        return e