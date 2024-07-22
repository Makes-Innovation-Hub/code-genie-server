import openai

def get_question_and_answer(topic):
    # this function sends a request to openai api to generate a question about any topic (it takes the topic as a parameter and returns the question and the answer as a dict)
    prompt = f"Generate a question and answer about the topic: {topic}"
    try:
        # Send the prompt to the OpenAI API using the ChatCompletion endpoint
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access to it
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,  # Adjust the number of tokens based on your needs
            temperature=0.7,
        )
        generated_text = response['choices'][0]['message']['content'].strip()
        
        # Split the generated text into question and answer
        lines = generated_text.split('\n')
        question = lines[0].strip() if lines else "No question generated"
        answer = lines[1].strip() if len(lines) > 1 else "No answer generated"

        return {"question": question, "answer": answer}
    except Exception as e:
        return {"error": str(e)}
