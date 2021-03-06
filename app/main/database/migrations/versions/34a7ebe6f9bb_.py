"""empty message

Revision ID: 34a7ebe6f9bb
Revises: 
Create Date: 2021-10-18 00:22:00.332375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34a7ebe6f9bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('github_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('avatar_url', sa.String(length=500), nullable=True),
    sa.Column('type', sa.String(length=20), nullable=False),
    sa.Column('url', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('github_users')
    # ### end Alembic commands ###
