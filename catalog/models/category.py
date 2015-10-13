from datetime import datetime
from urlparse import urljoin

from flask import url_for, request
from werkzeug import cached_property

from catalog import app, db
from catalog.helpers import slugify
from config import URL_UPLOAD_FOLDER

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_json(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            image=urljoin(request.url_root, self.image_src),
            recipes=[recipe.to_json() for recipe in self.recipes]
        )

    @cached_property
    def count(self):
        return self.recipes.count()

    @property
    def url(self):
        return url_for('recipes.category', id=self.id)

    @property
    def slug(self):
        return slugify(self.name)

    @property
    def image_src(self):
        return '/%s/categories/%s.png' % (URL_UPLOAD_FOLDER, self.id)

    def __repr__(self):
        return '<Category %r>' % (self.name)
