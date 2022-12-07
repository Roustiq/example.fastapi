"""create column to post table OMG

Revision ID: 4d1f74a1daf5
Revises: f9b4678f1cb2
Create Date: 2022-12-06 11:28:33.564035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d1f74a1daf5'
down_revision = 'f9b4678f1cb2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    pass

