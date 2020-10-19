"""empty message

Revision ID: 04fc0d55b4a6
Revises: 61d2e151ba72
Create Date: 2020-10-08 13:48:26.681068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04fc0d55b4a6'
down_revision = '61d2e151ba72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('total_votes', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_answer_total_votes'), 'answer', ['total_votes'], unique=False)
    op.drop_index('ix_answer_text', table_name='answer')
    op.create_index(op.f('ix_answer_text'), 'answer', ['text'], unique=False)
    op.add_column('question', sa.Column('description', sa.Text(), nullable=True))
    op.add_column('question', sa.Column('total_votes', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_question_description'), 'question', ['description'], unique=False)
    op.create_index(op.f('ix_question_total_votes'), 'question', ['total_votes'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_question_total_votes'), table_name='question')
    op.drop_index(op.f('ix_question_description'), table_name='question')
    op.drop_column('question', 'total_votes')
    op.drop_column('question', 'description')
    op.drop_index(op.f('ix_answer_text'), table_name='answer')
    op.create_index('ix_answer_text', 'answer', ['text'], unique=1)
    op.drop_index(op.f('ix_answer_total_votes'), table_name='answer')
    op.drop_column('answer', 'total_votes')
    # ### end Alembic commands ###
