from urlparse import urljoin
from datetime import datetime
from flask import url_for, request
from sqlalchemy import event

from catalog import db
from catalog.helpers import slugify, formated_time, delete_recipe_image
from config import URL_UPLOAD_FOLDER

class Recipe(db.Model):
    """Recipe model class.

    This class represents one recipe. Each recipe has an user id, category id, title, description, ingredients,
    preparation time, cook time, servings and a publish date. All fields are required.
    Two many to one relations are established between Recipe and Category and between Recipe and User tables.
    """

    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    ingredients = db.Column(db.String(), nullable=False)
    directions = db.Column(db.String(), nullable=False)
    prep_time = db.Column(db.Integer, nullable=False)
    cook_time = db.Column(db.Integer, nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    pub_date = db.Column(db.DateTime)

    user = db.relationship('User', backref=db.backref('recipes', cascade='delete, delete-orphan', lazy='dynamic'))
    category = db.relationship('Category', backref=db.backref('recipes', cascade='delete, delete-orphan', lazy='dynamic'))

    def __init__(self, user, category, title, description,
        ingredients, directions, prep_time, cook_time, servings, pub_date=None):
        self.user = user
        self.category = category
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.directions = directions
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.servings = servings

        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date

    def to_dict(self):
        """Converts recipe to dictionary."""

        return dict(
            id=self.id,
            category=dict(id=self.category_id, name=self.category.name),
            title=self.title,
            ingredients=self.ingredients,
            directions=self.directions,
            prep_time=self.prep_time,
            cook_time=self.cook_time,
            servings=self.servings,
            images=[image.to_dict() for image in self.images]
        )

    @property
    def formated_prep_time(self):
        return formated_time(self.prep_time)

    @property
    def formated_cook_time(self):
        return formated_time(self.cook_time)

    @property
    def url(self):
        return url_for('recipes.show', id=self.id)

    @property
    def slug(self):
        return slugify(self.title)

    @property
    def image_src(self):
        """Returns main recipe image. If none returns default image set for recipes."""

        if self.images.count() > 0 and self.images[0].filename:
            return '/%s/recipes/%s' % (URL_UPLOAD_FOLDER, self.images[0].filename)
        return '/static/images/no-image.png'

    def __repr__(self):
        return '<Recipe %r>' % (self.title)


class RecipeImage(db.Model):
    """"Recipe images model class.

    This class create the 'recipe_image' table. Each row will have an id, a recipe_id, a filename and a hidden column.
    All fields are required.

    A many to one relationship is established between this table and Recipe table.
    """
    __tablename__ = 'recipe_image'

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    filename = db.Column(db.String(250), nullable=False)
    hidden = db.Column(db.Boolean, nullable=False)

    recipe = db.relationship('Recipe', backref=db.backref('images', cascade='delete, delete-orphan', lazy='dynamic'))

    def __init__(self, recipe, filename, hidden=False):
        self.recipe = recipe
        self.filename = filename
        self.hidden = hidden

    def to_dict(self):
        return dict(src=urljoin(request.url_root, self.src))

    @property
    def src(self):
        return '/%s/recipes/%s' % (URL_UPLOAD_FOLDER, self.filename)

    @staticmethod
    def cb_delete_filename(mapper, connection, target):
        delete_recipe_image(target.filename)

    def __repr__(self):
        return '<Image %r %r>' % (self.id, self.recipe_id)

# delete filename from disk when 'after_delete' event is triggered
event.listen(RecipeImage, 'after_delete', RecipeImage.cb_delete_filename)
