import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db', 'recipes.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db', 'migrations')

WTF_CSRF_ENABLED = True
SECRET_KEY = '\x7f\x02\x03\xecy\xf1Q\xcc\xa7\x1c4h\xca\x88\xb8$\xd8S\xb1\xd9\x81\xbe\x8e\xeb'

OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '10153297467237872',
        'secret': 'b786b0a259bd059369c5e514fd3af124'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    }
}
# pagination
RECIPES_PER_PAGE = 3
# admin users
ADMIN = frozenset(['gersakbogdan@yahoo.com'])

del os
