def build_prompt(issue, context):
    return f"""You are an RTL verification assistant.

Issue:
{issue}

Retrieved Context:
{context}

Explain the root cause and suggest a Verilog/SystemVerilog fix.
"""
