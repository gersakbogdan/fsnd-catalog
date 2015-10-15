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
        'id': 'eWRZURJB2qtsSKHAdUVnirQLc',
        'secret': 'fozPwEFZ0rYkEnF9kMCC3IhdEyJSDgwPm9a28gsPv2gSjhs8Ly'
    },
    'google': {
        'id': '159773007921-1pqljrjflv1obbjsipuoa2ofrqd78g1r.apps.googleusercontent.com',
        'secret': 'ap4Ngq5DdNsEcJ7d41wG9BKm'
    }
}

# admin users email list
ADMIN = frozenset(['example@email.dom'])

UPLOAD_FOLDER = os.path.join(basedir, 'catalog', 'static', 'upload')
URL_UPLOAD_FOLDER = os.path.join('static', 'upload')

del os
