"""add users table

Revision ID: 652ca754266a
Revises: b9fa8ebf05a5
Create Date: 2023-02-05 16:22:04.598655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '652ca754266a'
down_revision = 'b9fa8ebf05a5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')                    
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
