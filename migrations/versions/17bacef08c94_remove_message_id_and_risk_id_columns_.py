"""remove message_id and risk_id columns from 'users' table

Revision ID: 17bacef08c94
Revises: c1476d0f3866
Create Date: 2022-04-28 22:08:37.643696

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "17bacef08c94"
down_revision = "c1476d0f3866"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("users_risk_id_fkey", "users", type_="foreignkey")
    op.drop_constraint("users_message_id_fkey", "users", type_="foreignkey")
    op.drop_column("users", "message_id")
    op.drop_column("users", "risk_id")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("risk_id", sa.INTEGER(), autoincrement=False, nullable=True)
    )
    op.add_column(
        "users",
        sa.Column("message_id", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.create_foreign_key(
        "users_message_id_fkey", "users", "messages", ["message_id"], ["id"]
    )
    op.create_foreign_key("users_risk_id_fkey", "users", "risks", ["risk_id"], ["id"])
    # ### end Alembic commands ###
