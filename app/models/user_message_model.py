from sqlalchemy import Column

from app.configs.database import db

users_messages = db.Table(
    "users_messages",
    Column("id", db.Integer, primary_key=True),
    Column("message_id", db.Integer, db.ForeignKey("messages.id")),
    Column("user_id", db.Integer, db.ForeignKey("users.id")),
)
