from flask import Blueprint, render_template, flash, request
from flask.ext.login import current_user, login_required

from catalog import db
from catalog.forms.recipe import RecipeForm
from catalog.models.recipe import Recipe, RecipeImage
from catalog.helpers import upload_recipe_image

mod = Blueprint('recipes', __name__, url_prefix='/recipes')

@mod.route('/<int:recipe_id>/<slug>/')
def view(recipe_id, slug):
    recipe = db.session.query(Recipe).filter_by(id=recipe_id).one()
    return render_template('recipes/view.html', recipe=recipe)

@mod.route('/my/')
@login_required
def index():
    recipes = db.session.query(Recipe) \
        .filter_by(user_id=current_user.id) \
        .order_by(Recipe.category_id.asc(),Recipe.title.asc()).all()
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
    recipe = db.session.query(Recipe).filter_by(id=recipe_id).one()
    form = RecipeForm(obj=recipe)

    if request.method == 'GET':
        pass
    elif recipe.user.id != current_user.id:
        flash(('danger', 'Oopss! It seems that you dont have the right to edit this recipe!'))
    elif form.validate_on_submit():
        recipe.user = current_user
        recipe.category = form.category.data
        recipe.title = form.title.data
        recipe.description = form.description.data
        recipe.ingredients = form.ingredients.data
        recipe.directions = form.directions.data
        recipe.prep_time = form.prep_time.data
        recipe.cook_time = form.cook_time.data
        recipe.servings = form.servings.data

        db.session.add(recipe)

        imagedata = form.image1.data
        if imagedata and imagedata.filename:
            filename = upload_recipe_image(imagedata)
            # save new entry into database
            image = RecipeImage(recipe, filename)
            db.session.add(image)

        # save database changes
        db.session.commit()
        flash(('success', 'Hooray! Your recipe was successfully edited!'))
    else:
        print form.errors.items()
        flash(('danger', 'Oopss! There are some issues to fix here...'))

    return render_template('recipes/edit.html', form=form, recipe_id=recipe.id, images=recipe.images)

@mod.route('/<int:recipe_id>/delete/', methods=['GET', 'POST'])
@login_required
def delete(recipe_id):
    if request.method == 'GET':
        return redirect(url_fo('recipes.index'))

    recipe = db.session.query(Recipe).filter_by(id=recipe_id).one()
    if recipe.user.id == current_user.id:
        db.session.delete(recipe)
        flash(('success', 'Recipe "%s" was successfully deleted!' % recipe.title))
        db.session.commit()
        return 'success'

    flash(('danger', 'Oopss! It seems that you dont have the right to delete this recipe!'))
    return 'error'

@mod.route('/<int:recipe_id>/image/<int:image_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_image(recipe_id, image_id):
    if request.method == 'GET':
        return redirect(url_fo('recipes.index'))

    recipe = db.session.query(Recipe).filter_by(id=recipe_id).one()
    if recipe.user.id == current_user.id:
        image = db.session.query(RecipeImage).filter_by(id=image_id).one()
        db.session.delete(image)
        flash(('success', 'Recipe image was successfully deleted!'))
        db.session.commit()
        return 'success'

    flash(('danger', 'Oopss! It seems that you dont have the right to delete this image!'))
    return 'error'

@mod.route('/category/<int:category_id>/')
def category(category_id):
    return render_template('recipes/category.html', )
