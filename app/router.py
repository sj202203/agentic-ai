import re
def router(text: str):
    t=text.lower().strip()

    # save note

    if t.startswith("save_note") or t.startswith("remember") or t.startswith("note"):
        note_text = text
        return{"tool":"save_note","args":{"text":note_text}}
    
    # read notes

    if any(phrase in t for phrase in ["search_notes","find note","look up note"]):
        query = text

        for phrase in ["search_notes","find note","look up note"]:
            if phrase in t:
                query = text.lower().split(phrase,1)[1].strip()
                break
        if not query:
            return {"tool":"unknown","args":{}}
        return {"tool":"search_notes","args":{"query":query}}
    
    # math

    nums = re.findall(r"-?\d+\.?\d*",t)

    if len(nums)>=2:
         a, b = float(nums[0]), float(nums[1])

         if any(symbol in t for symbol in ["plus","add","+"]):
             return {"tool":"calculator","args":{"a":a,"b":b,"op":"add"}}
         
         if any(symbol in t for symbol in ["minus","subtract","-"]):
             if "from" in t:
                 a,b = b,a
             return {"tool":"calculator","args":{"a":a,"b":b,"op":"sub"}}
         
         if any(symbol in t for symbol in ["multiply","times","*"]):
             return {"tool":"calculator","args":{"a":a,"b":b,"op":"mul"}}
         
         if any(symbol in t for symbol in ["divide","/"]):
             return {"tool":"calculator","args":{"a":a,"b":b,"op":"div"}}
    
    return {"tool":"unknown","args":{}}


