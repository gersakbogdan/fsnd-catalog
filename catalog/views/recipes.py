from flask import Blueprint, render_template, flash, request
from flask.ext.login import current_user, login_required

from catalog import db
from catalog.forms.recipe import RecipeForm
from catalog.models.recipe import Recipe, RecipeImage
from catalog.helpers import upload_recipe_image

mod = Blueprint('recipes', __name__, url_prefix='/recipes')

@mod.route('/<int:recipe_id>/<slug>')
def view(recipe_id):
    return render_template('recipes/view.html', recipe_id=recipe_id)

@mod.route('/my/')
@login_required
def index():
    recipes = db.session.query(Recipe).filter_by(user_id=current_user.id).all()
    return render_template('recipes/index.html', recipes=recipes)

@mod.route('/new/', methods=['GET', 'POST'])
@login_required
def new():
    form = RecipeForm()

    if request.method == 'GET':
        pass
    elif form.validate_on_submit():
        recipe = Recipe(current_user, form.category.data, form.title.data, form.description.data,
            form.ingredients.data, form.directions.data, form.prep_time.data, form.cook_time.data,
            form.servings.data
        )
        db.session.add(recipe)

        for imagedata in [form.image1.data, form.image2.data, form.image3.data]:
            if not imagedata.filename:
                continue
            filename = upload_recipe_image(imagedata)
            # save new entry into database
            image = RecipeImage(recipe, filename)
            db.session.add(image)

        # save database changes
        db.session.commit()
        flash(('success', 'Your recipe was successfully added!'))
    else:
        print form.errors.items()
        flash(('danger', 'Oopss! There are some issues to fix here...'))

    return render_template('recipes/new.html', form=form)

@mod.route('/<int:recipe_id>/edit/', methods=['GET', 'POST'])
@login_required
def edit(recipe_id):
    return render_template('recipes/edit.html', recipe_id=recipe_id)

@mod.route('/<int:recipe_id>/delete/', methods=['GET', 'POST'])
@login_required
def delete(recipe_id):
    return render_template('recipes/delete.html', recipe_id=recipe_id)

@mod.route('/category/<int:category_id>/')
def category(category_id):
    return render_template('recipes/category.html', )
