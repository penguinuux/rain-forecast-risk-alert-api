from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String


@dataclass
class AddressModel(db.Model):
    cep: str

    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    cep = Column(String(9), nullable=False)

    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
