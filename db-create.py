#!flask/bin/python

# Init/Create database
# Reference:
# http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from catalog import db
import os.path

db.create_all()

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'Database Repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(
        SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_MIGRATE_REPO,
        api.version(SQLALCHEMY_MIGRATE_REPO)
    )
