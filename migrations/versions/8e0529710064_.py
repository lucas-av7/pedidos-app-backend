"""empty message

Revision ID: 8e0529710064
Revises: 640609cb0315
Create Date: 2021-03-21 23:58:20.503050

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8e0529710064'
down_revision = '640609cb0315'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.Column('phone', sa.String(length=15), nullable=False),
                    sa.Column('password', sa.String(length=255), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    op.create_table('users_address',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('street', sa.String(length=150), nullable=False),
                    sa.Column('number', sa.String(length=30), nullable=False),
                    sa.Column('district', sa.String(length=50), nullable=False),
                    sa.Column('zipcode', sa.String(length=9), nullable=False),
                    sa.Column('city', sa.String(length=30), nullable=False),
                    sa.Column('state', sa.String(length=30), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
                    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
                    sa.Column('phone', sa.VARCHAR(length=15), autoincrement=False, nullable=False),
                    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='user_pkey'),
                    sa.UniqueConstraint('email', name='user_email_key')
                    )
    op.drop_table('users_address')
    op.drop_table('users')
    # ### end Alembic commands ###
