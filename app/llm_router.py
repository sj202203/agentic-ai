from ollama import chat
import json
from tools import *


MODEL = "qwen3:0.6b"

ROUTE_SCHEMA = {
    "type":"object",
    "properties":{
        "tool":{
            "type":"string",
            "enum":["calculator","save_note","read_notes","search_notes","unknown"]
        },
        "args":{
            "type": "object",
            "additionalProperties": True
    },
    },
    "required":["tool","args"],
    "additionalProperties": False
}

def llm_route(user_text: str):
    
    response = chat(
        model = MODEL,
        messages = [{"role":"user","content":user_text},{"role":"systemPrompt","content":"You must absolutely use tool calling to process user request."},{"role":"systemPrompt2","content":"If more than 1 tool calls are required,  use all which will be required."},{"role":"systemPrompt3","content":"for read_notes, search_notes or save_note function calls, use the complete user text along with the decision as the as the argument to these functions"}],
        tools = [calculator,save_note,read_notes,search_notes],
    )

    content = response.message.tool_calls

    return content