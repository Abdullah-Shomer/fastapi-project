"""add last few columns to posts table

Revision ID: c9beff71ad6b
Revises: 3388747ee7f7
Create Date: 2026-07-18 13:22:04.301601

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9beff71ad6b'
down_revision: Union[str, Sequence[str], None] = '3388747ee7f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, 
        Server_default='TRUE',))
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), 
        nullable=False, server_defult=sa.text('NEW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    
    pass
