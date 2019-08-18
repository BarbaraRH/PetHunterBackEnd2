"""empty message

Revision ID: 7df31999d1f2
Revises: f4a40f591d54
Create Date: 2019-08-17 23:53:37.200967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7df31999d1f2'
down_revision = 'f4a40f591d54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('adverts', sa.Column('district', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('adverts', 'district')
    # ### end Alembic commands ###
