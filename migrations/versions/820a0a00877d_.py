"""empty message

Revision ID: 820a0a00877d
Revises: 
Create Date: 2018-03-21 12:24:14.972812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '820a0a00877d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=80), nullable=True),
    sa.Column('lastname', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('date_joined', sa.DateTime(), nullable=True),
    sa.Column('filename', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###
