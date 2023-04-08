"""empty message

Revision ID: fb272c17d97f
Revises: b266480e0c8d
Create Date: 2023-04-08 13:28:47.683091

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fb272c17d97f'
down_revision = 'b266480e0c8d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('academics', 'education_level',
               existing_type=postgresql.ENUM('SCHOOL', 'HIGHSCHOOL', 'UNIVERSITY', name='enum_academic_type'),
               nullable=False)
    op.alter_column('academics', 'participant_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('account_controllers', 'address_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('account_controllers', 'participant_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('account_controllers_status', 'status',
               existing_type=postgresql.ENUM('VERIFIED', 'UNVERIFIED', 'TO_REVERIFIED', name='enum_account_controller_status'),
               nullable=False)
    op.alter_column('account_controllers_status', 'account_controller_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('balance_limits', 'amount',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('companies', 'participant_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('ethereum_accounts', 'public_key',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('government_organisms', 'participant_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('identifications', 'type',
               existing_type=postgresql.ENUM('DNI', 'CUIT', 'LE', name='enum_identification_type'),
               nullable=False)
    op.alter_column('identifications', 'person_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('natural_persons', 'participant_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('participants', 'type',
               existing_type=postgresql.ENUM('NATURAL_PERSON', 'GOVERNMENT_ORGANISM', 'COMPANY', 'ACADEMIC', name='enum_participant_type'),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('participants', 'type',
               existing_type=postgresql.ENUM('NATURAL_PERSON', 'GOVERNMENT_ORGANISM', 'COMPANY', 'ACADEMIC', name='enum_participant_type'),
               nullable=True)
    op.alter_column('natural_persons', 'participant_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('identifications', 'person_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('identifications', 'type',
               existing_type=postgresql.ENUM('DNI', 'CUIT', 'LE', name='enum_identification_type'),
               nullable=True)
    op.alter_column('government_organisms', 'participant_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('ethereum_accounts', 'public_key',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('companies', 'participant_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('balance_limits', 'amount',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('account_controllers_status', 'account_controller_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('account_controllers_status', 'status',
               existing_type=postgresql.ENUM('VERIFIED', 'UNVERIFIED', 'TO_REVERIFIED', name='enum_account_controller_status'),
               nullable=True)
    op.alter_column('account_controllers', 'participant_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('account_controllers', 'address_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('academics', 'participant_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('academics', 'education_level',
               existing_type=postgresql.ENUM('SCHOOL', 'HIGHSCHOOL', 'UNIVERSITY', name='enum_academic_type'),
               nullable=True)
    # ### end Alembic commands ###