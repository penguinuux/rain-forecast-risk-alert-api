from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String
from dataclasses import dataclass


@dataclass
class AddressModel(db.Model):
    id: int
    cep: str

    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    cep = Column(String(9), nullable=False)

    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
