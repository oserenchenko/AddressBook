"""add name index

Revision ID: 63b87b7d82d7
Revises: 450093542f15
Create Date: 2019-02-07 21:52:34.684448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63b87b7d82d7'
down_revision = '450093542f15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_addresses_name'), 'addresses', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_addresses_name'), table_name='addresses')
    # ### end Alembic commands ###
