"""create posts table

Revision ID: b638b7029f41
Revises: 
Create Date: 2024-10-03 20:00:18.716157

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b638b7029f41'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts",
                    sa.Column("id", sa.Integer,nullable=False,primary_key=True),
                    sa.Column("title", sa.String, nullable=False),
                    sa.Column("content", sa.String, nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),
                    sa.Column("published", sa.Boolean(), nullable=False, server_default='TRUE')
                    )

def downgrade() -> None:
    op.drop_table('posts')
    
