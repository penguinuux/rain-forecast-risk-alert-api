"""deleting description column from risk model

Revision ID: ed69951b98eb
Revises: c994f1b1ed8a
Create Date: 2022-05-03 19:08:14.301794

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "ed69951b98eb"
down_revision = "c994f1b1ed8a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("risks", "description")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "risks",
        sa.Column("description", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    # ### end Alembic commands ###
