from dataclasses import dataclass

from app.configs.database import db
from app.models.user_message_model import users_messages
from sqlalchemy import Column, DateTime, Integer, String


@dataclass
class MessageModel(db.Model):
    id: int
    title: str
    text: str
    date: str

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)

    users = db.relationship("UserModel", secondary=users_messages, backref="messages")
