from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine("sqlite:///soulledger.db", echo=True)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

def get_session():
    return SessionLocal()
