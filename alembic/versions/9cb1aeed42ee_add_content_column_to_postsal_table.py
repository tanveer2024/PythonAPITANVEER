"""add content column to postsal table

Revision ID: 9cb1aeed42ee
Revises: 136260eddf66
Create Date: 2022-08-26 12:32:24.466629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic. # alembic table witn "al"
revision = '9cb1aeed42ee'
down_revision = '136260eddf66'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('postsal', sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('postsal','content')
    pass
