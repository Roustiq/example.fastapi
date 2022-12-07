"""create column to post table again

Revision ID: f9b4678f1cb2
Revises: eed283003f02
Create Date: 2022-12-06 11:27:01.482260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9b4678f1cb2'
down_revision = 'eed283003f02'
branch_labels = None
depends_on = None


def upgrade() -> None:
    def upgrade() -> None:
        op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

