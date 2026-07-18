class OllamaClient:
    def __init__(self, model="llama3"):
        self.model=model

    def generate(self, prompt:str):
        raise NotImplementedError("Integrate Ollama API here.")
