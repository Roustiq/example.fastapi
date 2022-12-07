"""create column to post table

Revision ID: 14c3a67f6ba5
Revises: c49846c70e1f
Create Date: 2022-12-06 10:35:32.490976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14c3a67f6ba5'
down_revision = 'c49846c70e1f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
