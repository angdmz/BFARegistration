"""empty message

Revision ID: 659c35d2cf6c
Revises: bebb8d387d4d
Create Date: 2023-04-08 00:48:47.348661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '659c35d2cf6c'
down_revision = 'bebb8d387d4d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('account_controllers_participant_id_fkey', 'account_controllers', type_='foreignkey')
    op.create_foreign_key(None, 'account_controllers', 'participants', ['participant_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'account_controllers', type_='foreignkey')
    op.create_foreign_key('account_controllers_participant_id_fkey', 'account_controllers', 'natural_persons', ['participant_id'], ['id'])
    # ### end Alembic commands ###
