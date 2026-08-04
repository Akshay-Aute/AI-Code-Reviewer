# AI Code Reviewer

A Django-based web application for reviewing Python code.

## Features

- Python Syntax Highlighting (CodeMirror)
- PEP 8 Analysis
- Syntax Error Detection
- Quality Score
- Dashboard
- Code Suggestions
- Responsive Bootstrap UI

## Tech Stack

- Python
- Django
- Bootstrap 5
- CodeMirror
- pycodestyle
- AST

## Installation

```bash
git clone <repository-url>
cd AI-Code-Reviewer

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```