from database import get_session
from models import Entry, User, Tag
from datetime import datetime

session = get_session()

print("=== SoulLedger CLI ===")
print("1. View all entries")
print("2. Add new entry")
choice = input("Select an option: ")

if choice == "1":
    entries = session.query(Entry).all()
    for e in entries:
        print(f"[{e.date}] ({e.emotion}) {e.content[:50]}")

elif choice == "2":
    user_name = input("Enter your name: ")
    user = session.query(User).filter(User.name == user_name).first()
    if not user:
        print("User not found.")
    else:
        emotion = input("Emotion: ")
        content = input("Entry Content: ")
        tags_input = input("Comma-separated tags: ").split(",")
        tags = []
        for tag_name in tags_input:
            tag_name = tag_name.strip()
            tag = session.query(Tag).filter(Tag.name == tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                session.add(tag)
                session.flush()
            tags.append(tag)

        new_entry = Entry(emotion=emotion, content=content, user_id=user.id, tags=tags)
        session.add(new_entry)
        session.commit()
        print("✅ Entry added.")
