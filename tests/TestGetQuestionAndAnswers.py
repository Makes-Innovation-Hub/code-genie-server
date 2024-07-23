import pytest
from generate_questions.generate_question_4_answers import get_question_and_answers

def test_get_question_and_answers(mocker):
    mock_openai = mocker.patch('openai.ChatCompletion.create')
    mock_openai.return_value = {
        'choices': [
            {'message': {'content': 'Question: What is Python?\nCorrect Answer: Python is a programming language.\nWrong Answer 1: Python is a type of snake.\nWrong Answer 2: Python is a car model.\nWrong Answer 3: Python is a type of food.'}}
        ]
    }
    
    result = get_question_and_answers("Python")
    
    expected_result = {
        'question': 'What is Python?',
        'correct_answer': 'Python is a programming language.',
        'wrong_answers': [
            'Python is a type of snake.',
            'Python is a car model.',
            'Python is a type of food.'
        ]
    }
    assert result == expected_result
    
    # Verify the OpenAI API was called with the expected parameters
    mock_openai.assert_called_once_with(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": ("I need you to generate a new technical question for a computer science graduate about: Python. "
                                         "The question should have one correct answer and three incorrect answers. "
                                         "Format it as follows:\n"
                                         "Question: [your question]\n"
                                         "Correct Answer: [correct answer]\n"
                                         "Wrong Answer 1: [wrong answer 1]\n"
                                         "Wrong Answer 2: [wrong answer 2]\n"
                                         "Wrong Answer 3: [wrong answer 3]")}
        ],
        max_tokens=300,
        temperature=0.7
    )

if __name__ == '__main__':
    pytest.main()
