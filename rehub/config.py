import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "postgresql://rehub:rehub@localhost/rehub"

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
