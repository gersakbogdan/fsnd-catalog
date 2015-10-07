from catalog import db
from catalog.models.user import User
from catalog.models.category import Category

from datetime import datetime
from flask import url_for

class Recipe(db.Model):
    __tablename__ = 'recipes'
    __table_args__ = {'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    title = db.Column(db.String(250), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    prepare = db.Column(db.String)
    pub_date = db.Column(db.DateTime)

    user = db.relation(User, backref=db.backref('recipes', lazy='dynamic'))
    category = db.relation(Category, backref=db.backref('recipes', lazy='dynamic'))


    def __init__(self, user, category, title, ingredients, prepare):
        self.user = user
        self.category = category
        self.title = title
        self.ingredients = ingredients
        self.prepare = prepare
        self.pub_date = datetime.utcnow()

    def to_json(self):
        return dict(id=self.id,
                    user=self.author.name,
                    category=self.category.name,
                    title=self.title,
                    ingredients=self.ingredients,
                    prepare=self.prepare)

    @property
    def url(self):
        return url_for('recipes.show', id=self.id)

