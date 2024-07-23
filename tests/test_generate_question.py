import pytest
from unittest.mock import patch
from generateQuestions.generate_question import get_question_and_answer

class TestGetQuestionAndAnswer:

    @patch('openai.ChatCompletion.create')
    def test_get_question_and_answer(self, mock_openai):
        mock_openai.return_value = {
            'choices': [
                {'message': {'content': "What is the capital of France?\nParis"}}
            ]
        }
        topic = "Geography"
        result = get_question_and_answer(topic)

        assert result["question"] == "What is the capital of France?"
        assert result["answer"] == "Paris"

    @patch('openai.ChatCompletion.create')
    def test_get_question_and_answer_no_answer(self, mock_openai):
        # Mock an API response with no answer
        mock_openai.return_value = {
            'choices': [
                {'message': {'content': "What is the capital of France?"}}
            ]
        }
        topic = "Geography"
        result = get_question_and_answer(topic)

        assert result["question"] == "What is the capital of France?"
        assert result["answer"] == "No answer generated"

    @patch('openai.ChatCompletion.create')
    def test_get_question_and_answer_error(self, mock_openai):
        # Simulate an exception from the API
        mock_openai.side_effect = Exception("API error")
        topic = "Geography"
        result = get_question_and_answer(topic)

        assert "error" in result
        assert result["error"] == "API error"

if __name__ == '__main__':
    pytest.main()
