"""empty message

Revision ID: 020d98931178
Revises: 8e0529710064
Create Date: 2021-04-06 21:52:57.647978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '020d98931178'
down_revision = '8e0529710064'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('store',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('street', sa.String(length=150), nullable=False),
    sa.Column('number', sa.String(length=30), nullable=False),
    sa.Column('district', sa.String(length=50), nullable=False),
    sa.Column('city', sa.String(length=30), nullable=False),
    sa.Column('state', sa.String(length=30), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('store')
    # ### end Alembic commands ###
