"""add foreign key to posts table

Revision ID: 3388747ee7f7
Revises: 4ba6408e652c
Create Date: 2026-07-18 03:18:26.926542

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3388747ee7f7'
down_revision: Union[str, Sequence[str], None] = 'a31ae209675b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", 
                          referent_table="users",local_cols=['owner_id'], 
                          remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
