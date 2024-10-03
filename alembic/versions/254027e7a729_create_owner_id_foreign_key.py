"""create owner_id foreign key

Revision ID: 254027e7a729
Revises: 2fb923523f7a
Create Date: 2024-10-03 20:11:07.396900

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '254027e7a729'
down_revision: Union[str, None] = '2fb923523f7a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",
                  sa.Column('owner_id', sa.Integer(), nullable=False))
    
    op.create_foreign_key("posts_users_fk", source_table="posts", 
                          referent_table="users", local_cols=['owner_id'],
                          remote_cols=['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
