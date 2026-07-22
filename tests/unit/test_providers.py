from rtl_ai.llm.providers.openai_provider import OpenAIProvider

def test_provider():
    assert OpenAIProvider() is not None
