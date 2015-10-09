from catalog import db

from datetime import datetime
from flask import url_for

class Recipe(db.Model):
    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    ingredients = db.Column(db.String(999), nullable=False)
    directions = db.Column(db.String(999), nullable=False)
    prep_time = db.Column(db.Integer, nullable=False)
    cook_time = db.Column(db.Integer, nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    pub_date = db.Column(db.DateTime)


    def __init__(self, user_id, category_id, title, description, ingredients, directions, prep_time, cook_time, servings):
        self.user_id = user_id
        self.category_id = category_id
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.directions = directions
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.servings = servings
        self.pub_date = datetime.utcnow()

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

