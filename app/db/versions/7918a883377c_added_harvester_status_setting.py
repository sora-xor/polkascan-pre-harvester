"""Added harvester status setting

Revision ID: 7918a883377c
Revises: bd15422cbe5b
Create Date: 2019-09-27 13:52:20.525450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7918a883377c'
down_revision = 'bd15422cbe5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('harvester_setting',
    sa.Column('key', sa.String(length=64), nullable=False),
    sa.Column('value', sa.String(length=255), nullable=True),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('key')
    )
    op.create_table('harvester_status',
    sa.Column('key', sa.String(length=64), nullable=False),
    sa.Column('value', sa.String(length=255), nullable=True),
    sa.Column('last_modified', sa.DateTime(timezone=True), nullable=True),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('key')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('harvester_status')
    op.drop_table('harvester_setting')
    # ### end Alembic commands ###
