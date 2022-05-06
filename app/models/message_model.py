from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer

from app.configs.database import db


@dataclass
class MessageModel(db.Model):
    id: int
    date: str

    __tablename__ = "message_logs"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False, default=datetime.now())
