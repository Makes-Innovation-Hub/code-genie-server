import os
import pytest
from unittest.mock import patch, MagicMock
from services.openai_service import get_chat_completion

@pytest.fixture
def mock_openai_env(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test_api_key")

def test_get_chat_completion_failure(mock_openai_env):
    prompt = "Say hello to the world."
    
    # Mock an exception
    with patch('openai.ChatCompletion.create', side_effect=Exception("API error")):
        result = get_chat_completion(prompt)
        assert isinstance(result, Exception)
        assert str(result) == "API error"