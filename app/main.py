from router import router as fallback_route
from llm_router import llm_route
from tools import calculator, save_note, read_notes, search_notes
from memory import log_turn

def run_agent(user_txt: str):
    # try:
    decision = llm_route(user_txt)
    results = []
    # print(decision.function)
    # if not isinstance(decision,dict) or  "name" not in decision or "arguments" not in decision:
    #     raise ValueError("Bad LLM decision")
    # except Exception:
    #     print("Shit we are using fallback_route")
    #     decision = fallback_route(user_txt)

    for i in range (len(decision)):

        tool = decision[i].function.name
        args = decision[i].function.arguments

        if tool == "calculator":
            result = calculator(**args)
        
        elif tool == "save_note":
            txt = user_txt+f" function used : {tool} "+ "result: "+args['text']
            result = save_note(txt)
        
        elif tool == "read_notes":
            result = read_notes(**args)
        
        elif tool == "search_notes":
            result = search_notes(**args)
        
        else:
            result = "I do not understand the request."
        
        log_turn(user_txt,decision[i].function.name,str(result))
        results.append(result)
    return results

if __name__ == "__main__":
    print("Type quit to exit")

    while True:
        user_txt = input("\nYou: ").strip()

        if user_txt.lower() in ("quit","exit"):
            break
        print("Agent:",run_agent(user_txt))
