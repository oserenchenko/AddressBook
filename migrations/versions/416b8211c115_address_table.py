"""address table

Revision ID: 416b8211c115
Revises: 
Create Date: 2019-01-30 22:41:41.371867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '416b8211c115'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('zipcode', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_address_address'), 'address', ['address'], unique=True)
    op.create_index(op.f('ix_address_city'), 'address', ['city'], unique=True)
    op.create_index(op.f('ix_address_name'), 'address', ['name'], unique=True)
    op.create_index(op.f('ix_address_state'), 'address', ['state'], unique=True)
    op.create_index(op.f('ix_address_zipcode'), 'address', ['zipcode'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_address_zipcode'), table_name='address')
    op.drop_index(op.f('ix_address_state'), table_name='address')
    op.drop_index(op.f('ix_address_name'), table_name='address')
    op.drop_index(op.f('ix_address_city'), table_name='address')
    op.drop_index(op.f('ix_address_address'), table_name='address')
    op.drop_table('address')
    # ### end Alembic commands ###