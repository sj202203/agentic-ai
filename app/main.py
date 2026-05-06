from router import router
from tools import calculator, save_note, read_notes, search_notes
from memory import log_turn

def run_agent(user_txt: str):
    decision = router(user_txt)

    tool = decision["tool"]
    args = decision["args"]

    if tool == "calculator":
        result = calculator(**args)
    
    elif tool == "save_note":
        result = save_note(**args)
    
    elif tool == "read_notes":
        result = read_notes(**args)
    
    elif tool == "search_notes":
        result = search_notes(**args)
    
    else:
        result = "I do not understand the request."
    
    log_turn(user_txt,tool,str(result))
    return result

if __name__ == "__main__":
    print("Type quit to exit")

    while True:
        user_txt = input("\nYou: ").strip()

        if user_txt.lower() in ("quit","exit"):
            break
        print("Agent:",run_agent(user_txt))
