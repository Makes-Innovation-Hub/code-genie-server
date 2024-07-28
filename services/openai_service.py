import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))

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