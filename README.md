# 🧠 SoulLedger

**SoulLedger** is a terminal-based journaling system built using Python, SQLAlchemy, and SQLite.  
It allows users to log emotional entries, tag them with keywords, and explore their personal growth through structured data.

---

## 📌 Features

- 📝 Add journal entries with emotional labels (tags)
- 👤 Associate entries to individual users
- 🧠 Track recurring emotions or themes
- 🗂️ View past entries through CLI
- 🧪 SQLAlchemy ORM + SQLite backend

---

## 🛠️ Tech Stack

| Layer       | Tool              |
|-------------|-------------------|
| Language    | Python            |
| ORM         | SQLAlchemy        |
| Database    | SQLite            |
| Interface   | Terminal CLI      |
| Future UI   | Rich (Optional)   |

---

## 🚀 Getting Started

```bash
# Setup environment
python -m venv venv
venv\\Scripts\\activate  # Windows
source venv/bin/activate # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Seed with sample user and entries
python seed.py

# Launch CLI
python main.py
