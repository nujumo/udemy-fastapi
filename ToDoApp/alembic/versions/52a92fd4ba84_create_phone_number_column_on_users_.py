"""create phone_number column on users table

Revision ID: 52a92fd4ba84
Revises: 
Create Date: 2025-12-12 15:49:06.227824

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52a92fd4ba84'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(length=45), nullable=True))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')
    pass
