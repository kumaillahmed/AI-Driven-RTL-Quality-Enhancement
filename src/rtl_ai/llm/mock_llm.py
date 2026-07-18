from .base import BaseLLM

class MockLLM(BaseLLM):
    def generate(self, prompt:str)->str:
        return f"[Mock Response]\n{prompt[:200]}"
