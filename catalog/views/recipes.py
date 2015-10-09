from flask import Blueprint, render_template, flash
from flask.ext.login import current_user, login_required
from catalog import app, db
from catalog.forms.recipe import RecipeForm
from catalog.models.recipe import Recipe

mod = Blueprint('recipes', __name__, url_prefix='/recipes')

@mod.route('/')
def index():
    return render_template('recipes/index.html')

@mod.route('/new/', methods=['GET', 'POST'])
@login_required
def new():
    form = RecipeForm()
    if form.validate_on_submit():
        print 'form submitted'
        recipe = Recipe(
            current_user.id,
            form.category.data.id,
            form.title.data,
            form.description.data,
            form.ingredients.data,
            form.directions.data,
            form.prep_time.data,
            form.cook_time.data,
            form.servings.data
        )
        db.session.add(recipe)
        db.session.commit()
        flash('Your recipe was successfully added!')
    else:
        print form.errors.items()
    return render_template('recipes/new.html', form=form)

@mod.route('/edit/<int:id>/', methods=['GET', 'POST'])
@login_required
def edit(id):
    return render_template('recipes/edit.html', id=id)

@mod.route('/delete/<int:id>/', methods=['GET', 'POST'])
@login_required
def delete(id):
    return render_template('recipes/delete.html', id=id)
