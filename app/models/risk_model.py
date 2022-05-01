from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from app.configs.database import db


@dataclass
class RiskModel(db.Model):
    title: str
    description: str
    text: str

    # Rain precipitation limit in mm
    PRECIPITATION_LIMIT = 50

    __tablename__ = "risks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    text = Column(String, nullable=False)
