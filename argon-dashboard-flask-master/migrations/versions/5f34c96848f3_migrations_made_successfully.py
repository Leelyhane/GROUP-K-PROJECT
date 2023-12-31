"""Migrations Made Successfully

Revision ID: 5f34c96848f3
Revises: e74a3c3c526f
Create Date: 2023-07-26 16:51:05.883662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f34c96848f3'
down_revision = 'e74a3c3c526f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Intern_resumes', 'intern_id')
    op.drop_column('Job_resumes', 'job_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Job_resumes', sa.Column('job_id', sa.INTEGER(), nullable=True))
    op.add_column('Intern_resumes', sa.Column('intern_id', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
