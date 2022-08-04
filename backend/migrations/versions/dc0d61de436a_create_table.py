"""create table

Revision ID: dc0d61de436a
Revises: 
Create Date: 2022-07-30 15:46:45.120601

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dc0d61de436a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reception',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('expediteur', sa.String(length=50), nullable=True),
    sa.Column('id_expediteur', sa.Integer(), nullable=True),
    sa.Column('destinateur', sa.String(length=50), nullable=True),
    sa.Column('id_destinateur', sa.Integer(), nullable=True),
    sa.Column('message_', sa.TEXT, nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('heure', sa.Time(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reception_date'), 'reception', ['date'], unique=False)
    op.create_index(op.f('ix_reception_id'), 'reception', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=50), nullable=True),
    sa.Column('prenom', sa.String(length=50), nullable=True),
    sa.Column('categorie', mysql.ENUM('male', 'femme', 'autres'), nullable=True),
    sa.Column('mail', sa.String(length=50), nullable=True),
    sa.Column('telephone', sa.String(length=15), nullable=True),
    sa.Column('password', sa.String(length=6), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_reception_id'), table_name='reception')
    op.drop_index(op.f('ix_reception_date'), table_name='reception')
    op.drop_table('reception')
    # ### end Alembic commands ###
