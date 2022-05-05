from dataclasses import dataclass

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash

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
    password_hash = Column(String, nullable=False)

    address_id = Column(Integer, ForeignKey("addresses.id"), nullable=False)

    risks = relationship("RiskModel", secondary=user_risk, backref="users")
    address = relationship("AddressModel", backref="users", uselist=False)
    messages = relationship("MessageModel", secondary=users_messages, backref="users")

    VALIDATOR = {
        "name": {"type": str, "normalize": {str: "title"}},
        "phone": {"type": str, "unique": True},
        "email": {"type": str, "normalize": {str: "lower"}, "unique": True},
        "password": {"type": str},
        "cep": {"type": str},
    }

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_hash):
        return check_password_hash(self.password_hash, password_to_hash)
