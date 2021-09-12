"""empty message

Revision ID: 4528a2f4a269
Revises: 967967e33587
Create Date: 2021-09-11 22:38:18.020240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4528a2f4a269'
down_revision = '967967e33587'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('noaa_hourly_forecast',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('buoyid', sa.Integer(), nullable=False),
    sa.Column('starttime', sa.DateTime(), nullable=False),
    sa.Column('temp', sa.Integer(), nullable=True),
    sa.Column('windspeed', sa.Integer(), nullable=True),
    sa.Column('winddir', sa.String(), nullable=True),
    sa.Column('forecast', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('buoyid', 'starttime'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('noaa_hourly_forecast')
    # ### end Alembic commands ###
