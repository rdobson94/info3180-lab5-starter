"""empty message

Revision ID: e9d24ffd414d
Revises: 7fa41857a917
Create Date: 2017-02-25 01:51:56.325160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9d24ffd414d'
down_revision = '7fa41857a917'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'password')
    # ### end Alembic commands ###
