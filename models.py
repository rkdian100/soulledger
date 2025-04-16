from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

entry_tag_table = Table(
    'entry_tag', Base.metadata,
    Column('entry_id', Integer, ForeignKey('entries.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)
    entries = relationship("Entry", back_populates="user")
    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    emotion = Column(String(20))
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="entries")
    tags = relationship("Tag", secondary=entry_tag_table, back_populates="entries")
    def __repr__(self):
        return f"<Entry(emotion={self.emotion}, date={self.date})>"

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    entries = relationship("Entry", secondary=entry_tag_table, back_populates="tags")
    def __repr__(self):
        return f"<Tag(name={self.name})>"
