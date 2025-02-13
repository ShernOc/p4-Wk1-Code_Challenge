"""update feedback table

Revision ID: 08460e1be310
Revises: 4d33866b1a31
Create Date: 2025-01-23 18:03:15.735111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08460e1be310'
down_revision = '4d33866b1a31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedback',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('feedback_type', sa.Boolean(create_constraint=20), nullable=False),
    sa.Column('staff_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['staff_id'], ['staff.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('staff_feed')
    op.drop_table('user_feed')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_feed',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=128), nullable=False),
    sa.Column('description', sa.VARCHAR(length=256), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.Column('staff_id', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['staff_id'], ['staff.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('staff_feed',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=128), nullable=False),
    sa.Column('description', sa.VARCHAR(length=256), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.Column('staff_id', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['staff_id'], ['staff.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('feedback')
    # ### end Alembic commands ###
