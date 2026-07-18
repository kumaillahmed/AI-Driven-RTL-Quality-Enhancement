from rtl_ai.llm.mock_llm import MockLLM
from rtl_ai.llm.prompt_builder import build_prompt

def run(issue, context):
    llm = MockLLM()
    prompt = build_prompt(issue, context)
    return llm.generate(prompt)
