"""Demoversion

Revision ID: 1ea80e5f8b8b
Revises: 
Create Date: 2021-11-23 14:26:13.163332

"""

from os import getcwd
from os.path import join

import sqlalchemy as sa
from alembic import context, op


# revision identifiers, used by Alembic.
revision = '1ea80e5f8b8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('''
        CREATE TABLE IF NOT EXISTS DEMO_TABLE ( ID varchar(100) NOT NULL,
                                                DESCRIPTION varchar(100));
    ''')


def downgrade():
    op.execute('''
            DROP TABLE DEMO_TABLE;
        ''')
