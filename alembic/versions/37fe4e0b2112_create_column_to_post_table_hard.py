"""create column to post table hard

Revision ID: 37fe4e0b2112
Revises: 4d1f74a1daf5
Create Date: 2022-12-06 11:30:45.505191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37fe4e0b2112'
down_revision = '4d1f74a1daf5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    pass
