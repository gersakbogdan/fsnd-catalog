from catalog import app, db
from datetime import datetime
from flask.ext.login import UserMixin

class User(UserMixin, db.Model):
    """User model class.

    This class represents the 'user' table. It inherits from UserMixin which provides the required
    methods for LoginManager extension.
    Each row will have an id,social_id, name , email, picture and last seen column.
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    picture = db.Column(db.String(250))
    last_seen = db.Column(db.DateTime)

    def __init__(self, social_id, name, email, picture):
        self.social_id = social_id
        self.name = name
        self.email = email
        self.picture = picture
        self.last_seen = datetime.utcnow()

    @property
    def is_admin(self):
        """Check if user has admin rights."""

        return self.email in app.config['ADMIN']

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return '<User %r>' % (self.name)
