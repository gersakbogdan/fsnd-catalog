from flask import Blueprint, render_template, redirect, url_for, session, flash
from catalog import app, db
from catalog.models.category import Category
from catalog.models.recipe import Recipe

mod = Blueprint('general', __name__)

@mod.route('/')
def index():
    """Catalog main index page.

    Displays the list of popular categories and latest recipes.
    """

    recipes = db.session.query(Recipe).order_by(Recipe.id.desc()).limit(8).all()
    categories = db.session.query(Category).limit(6).all()
    return render_template('general/index.html', recipes=recipes, categories=categories)

@app.errorhandler(404)
def not_found(error):
    """404 Error handler method."""

    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """500 Error handler method."""

    db.session.rollback()
    return render_template('errors/500.html'), 500
