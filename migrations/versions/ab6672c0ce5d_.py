"""empty message

Revision ID: ab6672c0ce5d
Revises: 
Create Date: 2020-07-09 00:42:30.567486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab6672c0ce5d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('casinos',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('state', sa.String(length=20), nullable=True),
    sa.Column('zip_code', sa.String(length=14), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('time_zone', sa.String(length=50), nullable=True),
    sa.Column('website', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('facebook', sa.String(length=50), nullable=True),
    sa.Column('twitter', sa.String(length=50), nullable=True),
    sa.Column('instagram', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subscribers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(length=100), nullable=True),
    sa.Column('api_host', sa.String(length=100), nullable=True),
    sa.Column('api_token', sa.String(length=300), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('status', sa.Enum('valid', 'pending', 'unclaimed', 'pending_claim', name='userstatus'), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('nickname', sa.String(length=100), nullable=True),
    sa.Column('nationality', sa.String(length=30), nullable=True),
    sa.Column('hendon_url', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('tournaments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('casino_id', sa.String(length=10), nullable=True),
    sa.Column('multiday_id', sa.String(length=25), nullable=True),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('h1', sa.String(length=200), nullable=True),
    sa.Column('buy_in', sa.String(length=20), nullable=True),
    sa.Column('blinds', sa.String(length=20), nullable=True),
    sa.Column('starting_stack', sa.String(length=20), nullable=True),
    sa.Column('results_link', sa.String(length=500), nullable=True),
    sa.Column('structure_link', sa.String(length=500), nullable=True),
    sa.Column('start_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['casino_id'], ['casinos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flights',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tournament_id', sa.Integer(), nullable=True),
    sa.Column('start_at', sa.DateTime(), nullable=True),
    sa.Column('day', sa.String(length=5), nullable=True),
    sa.Column('notes', sa.String(length=3000), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['tournament_id'], ['tournaments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tournament_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('full_name', sa.String(length=40), nullable=True),
    sa.Column('nationality', sa.String(length=30), nullable=True),
    sa.Column('place', sa.String(length=6), nullable=True),
    sa.Column('winnings', sa.String(length=30), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['tournament_id'], ['tournaments.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    op.drop_table('flights')
    op.drop_table('tournaments')
    op.drop_table('users')
    op.drop_table('subscribers')
    op.drop_table('casinos')
    # ### end Alembic commands ###
