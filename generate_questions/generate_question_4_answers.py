import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_question_and_answers(topic):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    prompt = (f"I need you to generate a new technical question for a computer science graduate about: {topic}. "
              "The question should have one correct answer and three incorrect answers. "
              "Format it as follows:\n"
              "Question: [your question]\n"
              "Correct Answer: [correct answer]\n"
              "Wrong Answer 1: [wrong answer 1]\n"
              "Wrong Answer 2: [wrong answer 2]\n"
              "Wrong Answer 3: [wrong answer 3]")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,  # Increase the max_tokens to ensure the response is fully captured
            temperature=0.7,
        )
        
        generated_text = response['choices'][0]['message']['content'].strip()
        lines = generated_text.split('\n')

        question = None
        correct_answer = None
        wrong_answers = []

        for line in lines:
            if line.lower().startswith("question:"):
                question = line[len("Question:"):].strip()
            elif line.lower().startswith("correct answer:"):
                correct_answer = line[len("Correct Answer:"):].strip()
            elif line.lower().startswith("wrong answer 1:"):
                wrong_answers.append(line[len("Wrong Answer 1:"):].strip())
            elif line.lower().startswith("wrong answer 2:"):
                wrong_answers.append(line[len("Wrong Answer 2:"):].strip())
            elif line.lower().startswith("wrong answer 3:"):
                wrong_answers.append(line[len("Wrong Answer 3:"):].strip())

        if question is None or correct_answer is None or len(wrong_answers) != 3:
            raise ValueError("Failed to parse question and answers from the response.")

        return {
            "question": question,
            "correct_answer": correct_answer,
            "wrong_answers": wrong_answers
        }
    except Exception as e:
        return {"error": str(e)}
