"""add content column to posts table

Revision ID: a31ae209675b
Revises: ece725377584
Create Date: 2026-07-18 03:11:38.691454

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a31ae209675b'
down_revision: Union[str, Sequence[str], None] = 'ece725377584'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
def upgrade():
    op.add_column(
        'posts',
        sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')

    pass
