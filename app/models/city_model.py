from dataclasses import dataclass

from sqlalchemy import Column, ForeignKey, Integer, String

from app.configs.database import db


@dataclass
class CityModel(db.Model):
    name: str
    state_id: int

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    addresses = db.relationship("AddressModel", backref="cities")
