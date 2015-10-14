from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

# Init Flask app
# Reference: http://flask.pocoo.org/docs/0.10/quickstart/
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Init user session management
# Reference: https://flask-login.readthedocs.org/en/latest/
lm = LoginManager(app)
lm.login_view = 'general.index'
lm.login_message_category = 'danger'

# catalog.views dependencies list contains app package
# this this here to avoid cyclic imports
import catalog.views
