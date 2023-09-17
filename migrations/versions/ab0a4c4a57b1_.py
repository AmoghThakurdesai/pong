"""empty message

Revision ID: ab0a4c4a57b1
Revises: 7c272a162c06
Create Date: 2023-09-16 22:17:56.207290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab0a4c4a57b1'
down_revision = '7c272a162c06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player')
    op.drop_table('game')
    op.drop_table('gamerecord')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gamerecord',
    sa.Column('gameid', sa.INTEGER(), nullable=True),
    sa.Column('p1score', sa.INTEGER(), nullable=False),
    sa.Column('p2score', sa.INTEGER(), nullable=False),
    sa.Column('player1id', sa.INTEGER(), nullable=False),
    sa.Column('player2id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['player1id'], ['player.playerid'], ),
    sa.ForeignKeyConstraint(['player2id'], ['player.playerid'], ),
    sa.PrimaryKeyConstraint('p1score'),
    sa.UniqueConstraint('gameid')
    )
    op.create_table('game',
    sa.Column('recordid', sa.INTEGER(), nullable=False),
    sa.Column('gameid', sa.INTEGER(), nullable=True),
    sa.Column('p1score', sa.INTEGER(), nullable=True),
    sa.Column('p2score', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['gameid'], ['gamerecord.gameid'], ),
    sa.PrimaryKeyConstraint('recordid'),
    sa.UniqueConstraint('recordid')
    )
    op.create_table('player',
    sa.Column('playerid', sa.INTEGER(), nullable=True),
    sa.Column('username', sa.VARCHAR(), nullable=False),
    sa.Column('password', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('playerid'),
    sa.UniqueConstraint('playerid')
    )
    # ### end Alembic commands ###
