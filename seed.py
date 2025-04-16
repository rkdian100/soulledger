from database import get_session
from models import User, Entry, Tag
from datetime import datetime

session = get_session()

raj = User(name="Raj", age=30)
session.add(raj)
session.commit()

grief = Tag(name="grief")
discipline = Tag(name="discipline")
rebirth = Tag(name="rebirth")

session.add_all([grief, discipline, rebirth])
session.commit()

entry1 = Entry(
    emotion="grief",
    content="Today I cried again. But I wiped her tears before mine.",
    user_id=raj.id,
    tags=[grief]
)

entry2 = Entry(
    emotion="discipline",
    content="Didn't light the joint this morning. Bella is fed. Code is alive.",
    user_id=raj.id,
    tags=[discipline, rebirth]
)

session.add_all([entry1, entry2])
session.commit()

print("🌱 SoulLedger seeded successfully.")
