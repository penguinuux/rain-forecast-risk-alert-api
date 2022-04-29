from dataclasses import dataclass

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.configs.database import db

from .user_message_model import users_messages
from .user_risk_model import user_risk


@dataclass
class UserModel(db.Model):
    name: str
    phone: str
    email: str

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)

    address_id = Column(Integer, ForeignKey("addresses.id"), nullable=False)

    risks = relationship("RiskModel", secondary=user_risk, backref="users")
    address = relationship("AddressModel", backref="users", uselist=False)
    messages = relationship("MessageModel", secondary=users_messages, backref="users")
