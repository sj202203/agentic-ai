
# Agentic AI

Personal experiments with agentic, tool-using AI agents. This repository contains a minimal Python agent that performs simple math via a tool interface and saves conversation notes.

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

2. Install dependencies (create `requirements.txt` if not present):

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

- Add a `.gitignore` containing:

```
.venv/
__pycache__/
*.pyc
app/notes.txt
```

- Add a `requirements.txt` (use `pip freeze > requirements.txt` from your venv)
- Add a `LICENSE` file (e.g., MIT) if you want to make this public

## Contributing

This is a personal project for learning. If you want to collaborate, open an issue or send a pull request describing the change.

## License

Add a license file to indicate how you want others to reuse your work (suggestion: MIT).
