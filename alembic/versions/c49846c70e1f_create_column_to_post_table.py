"""create column to post table

Revision ID: c49846c70e1f
Revises: 5c2c077049ca
Create Date: 2022-12-06 10:19:34.056212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c49846c70e1f'
down_revision = '5c2c077049ca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
