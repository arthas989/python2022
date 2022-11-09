"""create an address table

Revision ID: c2f3a6618f82
Revises: 
Create Date: 2022-11-09 16:05:59.710651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c2f3a6618f82"
down_revision = None
branch_labels = None
depends_on = None

# 如果資料庫要upgrade，就會自動執行下列建立address table動作
def upgrade() -> None:
    op.create_table(
        "address",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("address", sa.String(50), nullable=False),
        sa.Column("city", sa.String(50), nullable=False),
        sa.Column("state", sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("address")
