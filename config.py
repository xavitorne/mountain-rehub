import os
basedir = os.path.abspath(os.path.dirname(__file__))

# if you have postgres use this uri:
SQLALCHEMY_DATABASE_URI = "postgresql://rehub:rehub@localhost/rehub"

# if you want to use sqlite, use this one:
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'rehub.db')

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

DEBUG=True
DATABASE=os.path.join(basedir, 'rehub.db')
USERNAME='admin'
PASSWORD='admin'
SECRET_KEY='$cippalippa!'
CSRF_ENABLED=True
