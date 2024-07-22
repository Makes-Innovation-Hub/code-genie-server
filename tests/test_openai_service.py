import os
import pytest
from services.openai_service import get_chat_completion

@pytest.fixture
def prompt():
    return "Say hello to the world."

def test_get_chat_completion(prompt):
    result = get_chat_completion(prompt)
    assert "hello" in result.lower()