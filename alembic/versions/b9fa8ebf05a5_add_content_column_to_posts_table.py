"""add content column to posts table

Revision ID: b9fa8ebf05a5
Revises: a19367701d54
Create Date: 2023-02-05 16:08:22.348305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9fa8ebf05a5'
down_revision = 'a19367701d54'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
