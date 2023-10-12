"""1_0_9

Revision ID: a521fbc28b18
Revises: b2f011d3a8b7
Create Date: 2023-09-28 13:37:16.479360

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a521fbc28b18'
down_revision = 'b2f011d3a8b7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        with op.batch_alter_table("downloadhistory") as batch_op:
            batch_op.add_column(sa.Column('date', sa.String, nullable=True))
            batch_op.add_column(sa.Column('channel', sa.String, nullable=True))
    except Exception as e:
        pass
    # ### end Alembic commands ###


def downgrade() -> None:
    pass
