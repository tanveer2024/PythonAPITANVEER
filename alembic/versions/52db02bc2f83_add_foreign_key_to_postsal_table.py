"""add foreign-key to postsal table

Revision ID: 52db02bc2f83
Revises: acaf5c0045d0
Create Date: 2022-08-26 15:21:01.054553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52db02bc2f83'
down_revision = 'acaf5c0045d0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('postsal',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('postsal_usersal_fk',source_table='postsal',referent_table='usersal',
    local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('postsal_usersal_fk',table_name='postsal')
    op.add_column('postsal','owner_id')
    pass
