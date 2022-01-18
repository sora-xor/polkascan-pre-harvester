"""Add XST Asset

Revision ID: 9a3ce0b237f5
Revises: 859005ea8024
Create Date: 2021-12-08 10:16:59.644076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a3ce0b237f5'
down_revision = '859005ea8024'
branch_labels = None
depends_on = None


def upgrade():
    sql_outcome = "insert into data_asset(asset_id, symbol, `precision`, is_mintable, name) " \
                  "values ('0x0200080000000000000000000000000000000000000000000000000000000000', 'XSTUSD', 18, 1, 'SORA Synthetic USD')"
    op.execute(sql_outcome)


def downgrade():
    pass
