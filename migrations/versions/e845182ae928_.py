"""empty message

Revision ID: e845182ae928
Revises: a5486c53b4c5
Create Date: 2021-06-29 18:27:11.688059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e845182ae928'
down_revision = 'a5486c53b4c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('casinos', sa.Column('subscriber', sa.String(length=20), nullable=True))
    op.add_column('flights', sa.Column('subscriber', sa.String(length=20), nullable=True))
    op.add_column('results', sa.Column('subscriber', sa.String(length=20), nullable=True))
    op.add_column('tournaments', sa.Column('subscriber', sa.String(length=25), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tournaments', 'subscriber')
    op.drop_column('results', 'subscriber')
    op.drop_column('flights', 'subscriber')
    op.drop_column('casinos', 'subscriber')
    # ### end Alembic commands ###
