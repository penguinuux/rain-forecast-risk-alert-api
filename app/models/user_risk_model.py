from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer

user_risk = db.Table(
    "user_risk",
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
    Column("risk_id", Integer, ForeignKey("risks.id")),
)
