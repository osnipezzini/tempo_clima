"""Alterado tipo do campo hora

Revision ID: f6b3997ecc26
Revises: 92ef94936108
Create Date: 2021-02-08 01:50:48.132687

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f6b3997ecc26'
down_revision = '92ef94936108'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('historico', sa.Column('data_pesquisa', sa.DateTime(), nullable=True))
    op.drop_column('historico', 'hora')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('historico', sa.Column('hora', postgresql.TIME(), autoincrement=False, nullable=True))
    op.drop_column('historico', 'data_pesquisa')
    # ### end Alembic commands ###