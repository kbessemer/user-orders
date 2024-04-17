"""Added order_item association table

Revision ID: d095823bbbe4
Revises: 12e3c58b700e
Create Date: 2024-04-16 14:58:00.618968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd095823bbbe4'
down_revision = '12e3c58b700e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_items')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_items',
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('item_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], name='order_items_item_id_fkey'),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], name='order_items_order_id_fkey'),
    sa.PrimaryKeyConstraint('order_id', 'item_id', name='order_items_pkey')
    )
    # ### end Alembic commands ###