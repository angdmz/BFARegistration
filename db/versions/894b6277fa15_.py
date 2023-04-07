"""empty message

Revision ID: 894b6277fa15
Revises: 28f4c5c2d06a
Create Date: 2023-04-06 22:49:29.752491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '894b6277fa15'
down_revision = '28f4c5c2d06a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('academics', sa.Column('participant_id', sa.UUID(), nullable=True))
    op.create_foreign_key(None, 'academics', 'participants', ['participant_id'], ['id'])
    op.add_column('companies', sa.Column('participant_id', sa.UUID(), nullable=True))
    op.create_foreign_key(None, 'companies', 'participants', ['participant_id'], ['id'])
    op.add_column('government_organisms', sa.Column('participant_id', sa.UUID(), nullable=True))
    op.create_foreign_key(None, 'government_organisms', 'participants', ['participant_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'government_organisms', type_='foreignkey')
    op.drop_column('government_organisms', 'participant_id')
    op.drop_constraint(None, 'companies', type_='foreignkey')
    op.drop_column('companies', 'participant_id')
    op.drop_constraint(None, 'academics', type_='foreignkey')
    op.drop_column('academics', 'participant_id')
    # ### end Alembic commands ###