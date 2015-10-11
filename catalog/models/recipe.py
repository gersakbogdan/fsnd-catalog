from catalog import db
from datetime import datetime
from flask import url_for

from config import URL_UPLOAD_FOLDER

class Recipe(db.Model):
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

    def to_json(self):
        return dict(id=self.id,
                    title=self.title,
                    ingredients=self.ingredients,
                    directions=self.directions,
                    prep_time=self.prep_time,
                    cook_time=self.cook_time,
                    servings=self.servings)

    @property
    def url(self):
        return url_for('recipes.show', id=self.id)

    @property
    def image_src(self):
        if self.images.count() > 0 and self.images[0].filename:
            return '/%s/recipes/%s' % (URL_UPLOAD_FOLDER, self.images[0].filename)
        return '/static/images/no-image.png'

    def __repr__(self):
        return '<Recipe %r>' % (self.title)


class RecipeImage(db.Model):
    __tablename__ = 'recipe_image'

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    filename = db.Column(db.String(250), nullable=False)
    hidden = db.Column(db.Boolean, nullable=False)

    recipe = db.relationship('Recipe', backref=db.backref('images', lazy='dynamic'))

    def __init__(self, recipe, filename, hidden=False):
        self.recipe = recipe
        self.filename = filename
        self.hidden = hidden

    @property
    def src(self):
        return '/%s/recipes/%s' % (URL_UPLOAD_FOLDER, self.filename)

    def __repr__(self):
        return '<Image %r %r>' % (self.id, self.recipe_id)
