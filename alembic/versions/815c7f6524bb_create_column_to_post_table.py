"""create column to post table

Revision ID: 815c7f6524bb
Revises: 14c3a67f6ba5
Create Date: 2022-12-06 10:39:56.862200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '815c7f6524bb'
down_revision = '14c3a67f6ba5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
