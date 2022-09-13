"""add few columns to postsal table

Revision ID: 0de9f8e5c1a1
Revises: 52db02bc2f83
Create Date: 2022-08-26 15:38:28.118441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0de9f8e5c1a1'
down_revision = '52db02bc2f83'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('postsal',sa.Column(
        'published',sa.Boolean(),nullable=False,server_default='True'
    ))
    op.add_column('postsal',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')
    ))
    pass


def downgrade():
    op.drop_column('postsal', 'published')
    op.drop_column('postsal','created_at')
    pass
