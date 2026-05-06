from datetime import datetime

NOTE_FILE = "notes.txt"

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
    with open(NOTE_FILE, "a", encoding = "utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}] {text}\n")
    return f"Saved Note: {text}"


def read_notes(limit: int=5):
    """Read all notes from notes.txt."""
    
    try:
        with open(NOTE_FILE,"r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return "No notes found"
    
    lines = [line.rstrip("\n") for line in lines if line.strip()]

    if not lines:
        return "No notes found"
    
    return "\n".join(lines[-limit:])

def search_notes(query: str):
    """Searches all notes from notes.txt"""
    try:
        with open(NOTE_FILE,"r",encoding="utf-8") as f:
            lines=f.readlines()
    except FileNotFoundError:
        return "No notes found"
    
    query = query.lower().strip()
    matches = [line.rstrip("\n") for line in lines if query in line.lower()]

    if not matches:
        return f'No notes found for "{query}".'
    
    return "\n".join(matches)
    