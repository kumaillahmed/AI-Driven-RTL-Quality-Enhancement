class OpenAIClient:
    def __init__(self, api_key=None, model="gpt-4.1"):
        self.api_key=api_key
        self.model=model

    def generate(self, prompt:str):
        raise NotImplementedError("Integrate OpenAI SDK here.")
