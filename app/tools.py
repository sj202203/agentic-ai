from datetime import datetime

def calculator(a: float, b: float, op: str):
    """Do basic math on two numbers.

    Args:
        a: First number
        b: Second number
        op: One of add, sub, mul, div
    """

    if op in ("add", "+"):
        return a + b
    if op in ("sub", "-"):
        return a - b
    if op in ("mul", "*"):
        return a * b
    if op in ("div", "/"):
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    return "Unknown operation"


def save_note(text: str):
    """Save a note to notes.txt. When called, you need to store the whole user txt like what all the user has asked, the decision that the llm took and the final result.

    Args:
        text: Note text
    """
    with open("notes.txt", "a", encoding = "utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}] {text}\n")
    return f"Saved Note: {text}"