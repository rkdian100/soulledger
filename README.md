# SoulLedger (Raw Push Version)

Initial version of SoulLedger — a simple journaling CLI tool built with SQLAlchemy and SQLite.

## Features

- Add entries tagged with emotions
- View past entries in terminal
- Multi-user and multi-tag support (ORM-based)

## Setup

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate # macOS/Linux

pip install -r requirements.txt
python seed.py
python main.py
```

## Next Updates

- Add Rich-based CLI interface
- Deletion and filtering features
- Export to JSON
