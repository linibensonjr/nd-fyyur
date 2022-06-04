"""empty message

Revision ID: 38d084d925ce
Revises: 56af51d19d88
Create Date: 2022-06-03 23:20:22.405593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38d084d925ce'
down_revision = '56af51d19d88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genres', sa.ARRAY(sa.String()), server_default='{}', nullable=True))
    op.drop_column('Venue', 'genre')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genre', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'genres')
    # ### end Alembic commands ###
