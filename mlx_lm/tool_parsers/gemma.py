import json

tool_call_start = "```tool_code"

tool_call_end = "```"


def parse_tool_call(text, tools=None):

    try:
        structured = json.loads(text.strip())
    except:
        raise ValueError("Invalid JSON provided: {text}")

    if type(structured) is list:
        structured = structured[0]

    structured = structured.get("function", structured)

    return structured
