from sqlalchemy import Column

from app.configs.database import db

users_messages = db.Table(
    "users_messages",
    Column("id", db.Integer, primary_key=True),
    Column("message_log_id", db.Integer, db.ForeignKey("message_logs.id")),
    Column("user_id", db.Integer, db.ForeignKey("users.id")),
)
