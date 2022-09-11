"""create postsal table

Revision ID: 136260eddf66
Revises: 
Create Date: 2022-08-26 12:02:31.023788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '136260eddf66' # postsal table # all table with alembic ends with "al"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('postsal',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('postsal')
    pass
