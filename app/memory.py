import json
from datetime import datetime

MEMORY_FILE="memeory.jsonl"

def log_turn(user_text: str, decision: dict, result: str):
    entry = {
        "time":datetime.now().isoformat(),
        "user_txt": user_text,
        "decision": decision,
        "result": result
    }

    with open(MEMORY_FILE,"a",encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")