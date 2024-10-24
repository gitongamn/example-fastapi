"""add content column to posts table

Revision ID: 02479ecea3e9
Revises: d1a3305878fd
Create Date: 2024-10-19 10:11:50.989413

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02479ecea3e9'
down_revision: Union[str, None] = 'd1a3305878fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
