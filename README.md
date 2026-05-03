# Agentic AI

Personal experiments with agentic, tool-using AI agents. This repository contains a minimal Python agent that performs simple math via a tool interface and saves conversation notes.

## Files added

- `requirements.txt` — pinned dependencies generated from the repository virtual environment
- `.gitignore` — ignores local environment and artifacts (e.g., `.venv`, `__pycache__`, `app/notes.txt`)

## Features

- Tool-based assistant that delegates math operations to a `calculator` tool
- Saves agent decisions and results to `app/notes.txt` (local note log)

## Prerequisites

- Python 3.10+ recommended
- Create and activate a virtual environment before installing dependencies

## Quickstart

1. Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the agent:

```bash
python app/main.py
```

Type `exit` or `quit` to stop the agent.

## Security & Privacy

- `app/notes.txt` contains saved conversation history and may hold sensitive or private prompts/results. Do not publish it publicly. Consider redacting or excluding it from the repo.
- Do not commit the virtual environment (`.venv/`) or `__pycache__/` to source control. Use a `.gitignore` to exclude them.

## Recommended repository housekeeping

- The repository already includes a `.gitignore` and `requirements.txt`. Ensure you do not add `.venv` to git history if it was previously committed.
- Example `.gitignore` entries (already applied):

```
.venv/
__pycache__/
*.pyc
app/notes.txt
.env
.vscode/
```

## Contributing

This is a personal project for learning. If you want to collaborate, open an issue or send a pull request describing the change.


