from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship


@dataclass
class StateModel(db.Model):

    name: str

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    cities = relationship("CityModel", backref=backref("state", uselist=False))
