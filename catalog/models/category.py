from catalog import app, db
from datetime import datetime

from config import URL_UPLOAD_FOLDER

from werkzeug import cached_property
from flask import url_for

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_json(self):
        return dict(name=self.name, description=self.description)

    @cached_property
    def count(self):
        return self.recipes.count()

    @property
    def url(self):
        return url_for('recipes.category', id=self.id)

    @property
    def image_src(self):
        return '/%s/categories/%s.png' % (URL_UPLOAD_FOLDER, self.id)

    def __repr__(self):
        return '<Category %r>' % (self.name)
