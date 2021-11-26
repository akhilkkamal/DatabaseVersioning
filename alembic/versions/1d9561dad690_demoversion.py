"""Demoversion

Revision ID: 1d9561dad690
Revises: 1ea80e5f8b8b
Create Date: 2021-11-26 15:31:54.108262

"""

from os import getcwd
from os.path import join

import sqlalchemy as sa
from alembic import context, op


# revision identifiers, used by Alembic.
revision = '1d9561dad690'
down_revision = '1ea80e5f8b8b'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('''
            INSERT INTO DEMO_TABLE ( ID,DESCRIPTION) VALUES('1','Test');
        ''')


def downgrade():
    op.execute('''
                DELETE FROM DEMO_TABLE ;
            ''')
