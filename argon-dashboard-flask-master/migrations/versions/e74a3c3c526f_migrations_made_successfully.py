"""Migrations Made Successfully

Revision ID: e74a3c3c526f
Revises: 66f8573e87bd
Create Date: 2023-07-26 16:21:07.952016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e74a3c3c526f'
down_revision = '66f8573e87bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Intern_resumes',
    sa.Column('resume_id', sa.Integer(), nullable=False),
    sa.Column('intern_id', sa.Integer(), nullable=True, foreign_keys=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('resume_file', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('resume_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('resume_id')
    )
    op.create_table('Internships',
    sa.Column('intern_id', sa.Integer(), nullable=False),
    sa.Column('job_type', sa.String(length=64), nullable=True),
    sa.Column('intern_name', sa.String(length=64), nullable=True),
    sa.Column('company', sa.String(length=64), nullable=True),
    sa.Column('locaion', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('application_deadline', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('intern_id'),
    sa.UniqueConstraint('intern_id')
    )
    op.create_table('Job_listings',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('job_type', sa.String(length=64), nullable=True),
    sa.Column('job_name', sa.String(length=64), nullable=True),
    sa.Column('company', sa.String(length=64), nullable=True),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('desription', sa.String(length=255), nullable=True),
    sa.Column('application_deadline', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('job_id'),
    sa.UniqueConstraint('job_id')
    )
    op.create_table('Job_resumes',
    sa.Column('resume_id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True, foreign_keys=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('resume_file', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('resume_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('resume_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Job_resumes')
    op.drop_table('Job_listings')
    op.drop_table('Internships')
    op.drop_table('Intern_resumes')
    # ### end Alembic commands ###
