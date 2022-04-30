from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String


@dataclass
class RiskModel(db.Model):

    title: str
    description: str
    text: str

    __tablename__ = "risks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    text = Column(String, nullable=False)
