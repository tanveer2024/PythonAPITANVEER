"""add useral table

Revision ID: acaf5c0045d0
Revises: 9cb1aeed42ee
Create Date: 2022-08-26 14:54:20.238664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acaf5c0045d0' # useral table
down_revision = '9cb1aeed42ee'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('usersal', # check if useral or usersal
                     sa.Column('id',sa.Integer(),nullable=False),
                     sa.Column('email',sa.String(),nullable=False),
                     sa.Column('password',sa.String(),nullable=False),
                     sa.Column('created_at',sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
                     sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email')
                     )
    pass


def downgrade():
    op.drop_table('usersal')
    pass
