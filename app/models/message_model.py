from dataclasses import dataclass

from sqlalchemy import Column, DateTime, Integer, String

from app.configs.database import db


@dataclass
class MessageModel(db.Model):
    title: str
    text: str
    date: str

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
