from sqlalchemy import Column, Integer, String, TIMESTAMP, TEXT
from ..database import db


class LoggerModel(db.Model):
    __tablename__ = 'logger'

    id = Column(Integer, primary_key=True)
    message = Column(String(255))
    level_name = Column(String(50))
    timestamp = Column(TIMESTAMP)
    source = Column(String(255))
    context = Column(TEXT)

    def __init__(self, message, level_name, timestamp, source, context) -> None:
        self.message = message
        self.level_name = level_name
        self.timestamp = timestamp
        self.source = source
        self.context = context

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
