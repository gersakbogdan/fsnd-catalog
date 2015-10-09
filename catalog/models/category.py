from catalog import app, db
from datetime import datetime

from werkzeug import cached_property

from flask import url_for

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(150), nullable=False)

    def __init__(self, name):
        self.name = name
        self.slug = '-'.join(name.split()).lower()

    def to_json(self):
        return dict(name=self.name, slug=self.slug, count=self.count)

    @cached_property
    def count(self):
        return self.recipes.count()

    @property
    def url(self):
        return url_for('recipes.category', slug=self.slug)

    def __repr__(self):
        return '<Category %r>' % (self.name)
