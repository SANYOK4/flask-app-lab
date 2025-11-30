"""populate categories

Revision ID: 4e7c6544aae6
Revises: 3fa5f3a022a6
Create Date: 2025-11-30 21:36:45.443023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e7c6544aae6'
down_revision = '3fa5f3a022a6'
branch_labels = None
depends_on = None


def upgrade():
    categories_table = sa.table('categories',
        sa.column('id', sa.Integer()),
        sa.column('name', sa.String())
    )


    op.bulk_insert(categories_table, [
        {'name': 'Phones'},
        {'name': 'Tablets'},
        {'name': 'Accessories'}
    ])


def downgrade():
    pass
