import time
from urlparse import urljoin

from flask import url_for, request
from werkzeug import cached_property

from catalog import app, db
from catalog.helpers import slugify
from config import URL_UPLOAD_FOLDER

class Category(db.Model):
    """"Category model class.

    This class represents one category. Each category has a name, a description and one image. All fields are required.
    """

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_dict(self):
        """Converts recipe to dictionary."""

        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            image=urljoin(request.url_root, self.image_src),
            recipes=[recipe.to_dict() for recipe in self.recipes]
        )

    @cached_property
    def count(self):
        return self.recipes.count()

    @property
    def slug(self):
        return slugify(self.name)

    @property
    def image_src(self):
        return '/%s/categories/%s.png?%s' % (URL_UPLOAD_FOLDER, self.id, int(time.time()))

    def __repr__(self):
        return '<Category %r>' % (self.name)
