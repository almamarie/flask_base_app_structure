"""
Adding a loging table to store logs

Revision ID: ed321e60dc53
Revises: 25c20e915104
Create Date: 2023-11-20 00:41:01.005983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed321e60dc53'
down_revision = '25c20e915104'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logger',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('message', sa.String(length=255), nullable=True),
                    sa.Column('level_name', sa.String(
                        length=50), nullable=True),
                    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
                    sa.Column('source', sa.String(length=255), nullable=True),
                    sa.Column('context', sa.TEXT(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('logger')
    # ### end Alembic commands ###
