"""rename column message_id to message_log_id from table 'users_messages'

Revision ID: 0c2695d21bef
Revises: 4785f95a9c8f
Create Date: 2022-05-03 23:23:10.764430

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0c2695d21bef"
down_revision = "4785f95a9c8f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users_messages", sa.Column("message_log_id", sa.Integer(), nullable=True)
    )
    op.drop_constraint(
        "users_messages_message_id_fkey", "users_messages", type_="foreignkey"
    )
    op.create_foreign_key(
        None, "users_messages", "message_logs", ["message_log_id"], ["id"]
    )
    op.drop_column("users_messages", "message_id")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users_messages",
        sa.Column("message_id", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.drop_constraint(None, "users_messages", type_="foreignkey")
    op.create_foreign_key(
        "users_messages_message_id_fkey",
        "users_messages",
        "message_logs",
        ["message_id"],
        ["id"],
    )
    op.drop_column("users_messages", "message_log_id")
    # ### end Alembic commands ###
