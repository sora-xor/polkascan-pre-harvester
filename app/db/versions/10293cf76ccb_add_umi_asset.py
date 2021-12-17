"""Add UMI Asset

Revision ID: 10293cf76ccb
Revises: 9a3ce0b237f5
Create Date: 2021-12-17 12:54:54.794572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10293cf76ccb'
down_revision = '9a3ce0b237f5'
branch_labels = None
depends_on = None


def upgrade():
    sql_outcome = "insert into data_asset(asset_id, symbol, `precision`, is_mintable, name) " \
                  "values ('0x003252667a82d2dd70fa046eea663eaec1f2e37c20879f113b880b04c5ebd805', 'UMI', 18, 1, 'UmiToken')"
    op.execute(sql_outcome)



def downgrade():
    pass
