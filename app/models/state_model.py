from dataclasses import dataclass

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref, relationship

from app.configs.database import db


@dataclass
class StateModel(db.Model):
    name: str
    uf: str

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    uf = Column(String(2), nullable=False)

    cities = relationship("CityModel", backref=backref("state", uselist=False))
