"""add user table

Revision ID: 30670c5a5da6
Revises: 815c7f6524bb
Create Date: 2022-12-06 10:49:49.592017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30670c5a5da6'
down_revision = '815c7f6524bb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
