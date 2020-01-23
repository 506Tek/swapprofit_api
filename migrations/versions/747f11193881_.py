"""empty message

Revision ID: 747f11193881
Revises: eb0af20ad97e
Create Date: 2020-01-23 05:41:25.205598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '747f11193881'
down_revision = 'eb0af20ad97e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tournaments', sa.Column('linds', sa.String(length=20), nullable=True))
    op.drop_column('tournaments', 'blinds')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tournaments', sa.Column('blinds', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('tournaments', 'linds')
    # ### end Alembic commands ###
