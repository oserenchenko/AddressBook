"""addresses table

Revision ID: 450093542f15
Revises: 
Create Date: 2019-02-07 21:52:12.581848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '450093542f15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('zipcode', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('addresses')
    # ### end Alembic commands ###
