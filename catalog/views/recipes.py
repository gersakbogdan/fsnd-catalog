from xmltodict import unparse
from flask import Blueprint, render_template, flash, request, redirect, url_for, jsonify, Response
from flask.ext.login import current_user, login_required

from catalog import db
from catalog.forms.recipe import RecipeForm
from catalog.models.category import Category
from catalog.models.recipe import Recipe, RecipeImage
from catalog.helpers import upload_recipe_image, csrf_protect

mod = Blueprint('recipes', __name__, url_prefix='/recipes')

@mod.route('/<int:recipe_id>/<slug>/')
def view(recipe_id, slug):
    """Recipe details page.

    Displays the recipe details if is found, if not a redirect to the index page is triggered.

    Args:
        recipe_id: The id of recipe to display
        slug: Recipe title but only with valid url chars. Used for SEO reasons only.
    """

    try:
        recipe = db.session.query(Recipe).filter_by(id=recipe_id).one()
    except:
        return redirect(url_for('general.index'))

    return render_template('recipes/view.html', recipe=recipe)

@mod.route('/my/')
@login_required
def index():
    """User recipes list.

    Displays a list of users recipes grouped by category and ordered by name.
    """

    recipes = db.session.query(Recipe) \
        .filter_by(user_id=current_user.id) \
        .order_by(Recipe.category_id.asc(),Recipe.title.asc()).all()
    return render_template('recipes/index.html', recipes=recipes)

@mod.route('/new/', methods=['GET', 'POST'])
@login_required
def new():
    """Add recipe page.

    Displays the form to add a new recipe.
    If the form is successfully submitted an success message is shown.
    This page can be accessed only by logged in users.
    """

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
        flash('Your recipe was successfully added!', 'success')
        return redirect(url_for('recipes.view', recipe_id=recipe.id, slug=recipe.slug))
    else:
        print form.errors.items()
        flash('Oopss! There are some issues to fix here...', 'danger')

    return render_template('recipes/new.html', form=form)

@mod.route('/<int:recipe_id>/edit/', methods=['GET', 'POST'])
@login_required
def edit(recipe_id):
    """Recipe edit page.

    Displays the form to edit a recipe.
    This page can be accessed only by logged in users.

    Args:
        recipe_id: The recipe id to be edit
    """

    try:
        recipe = db.session.query(Recipe).filter_by(id=recipe_id).one()
    except:
        flash('Oopss! The recipe does not exists!', 'danger')
        return redirect(url_for('recipes.index'))

    form = RecipeForm(obj=recipe)

    if request.method == 'GET':
        pass
    elif recipe.user.id != current_user.id:
        flash('Oopss! It seems that you dont have the right to edit this recipe!', 'danger')
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
        flash('Hooray! Your recipe was successfully edited!', 'success')
        return redirect(url_for('recipes.view', recipe_id=recipe.id, slug=recipe.slug))
    else:
        print form.errors.items()
        flash('Oopss! There are some issues to fix here...', 'danger')

    return render_template('recipes/edit.html', form=form, recipe_id=recipe.id, images=recipe.images)

@mod.route('/<int:recipe_id>/delete/', methods=['GET', 'POST'])
@login_required
def delete(recipe_id):
    """Delete recipe handler.

    Deletes the recipe from the database if exists. All the associated images will also be deleted.
    This page can be accessed only by logged in users and CSRF check runs for each delete.

    Args:
        recipe_id: The recipe id to be deleted
    """

    if request.method == 'GET':
        return redirect(url_fo('recipes.index'))

    csrf_protect() # csrf protection
    try:
        recipe = db.session.query(Recipe).filter_by(id=recipe_id).one()
    except:
        flash('Oopss! The recipe does not exists!', 'danger')
        return redirect(url_for('recipes.index'))

    if recipe.user.id == current_user.id:
        db.session.delete(recipe)
        flash('Recipe "%s" was successfully deleted!' % recipe.title, 'success')
        db.session.commit()
        return 'success'

    flash('Oopss! It seems that you dont have the right to delete this recipe!', 'danger')
    return 'error'

@mod.route('/<int:recipe_id>/image/<int:image_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_image(recipe_id, image_id):
    """Delete recipe images handler.

    Deletes one recipe image from the database if exists.
    This page can be accessed only by logged in users and CSRF check runs for each delete.

    Args:
        recipe_id: The recipe id to be deleted
        image_id: The image id to be deleted
    """

    if request.method == 'GET':
        return redirect(url_fo('recipes.index'))

    csrf_protect() # csrf protection

    try:
        recipe = db.session.query(Recipe).filter_by(id=recipe_id).one()
    except:
        flash('Oopss! The recipe image does not exists!', 'danger')
        return redirect(url_for('recipes.index'))

    if recipe.user.id == current_user.id:
        image = db.session.query(RecipeImage).filter_by(id=image_id).one()
        db.session.delete(image)
        flash('Recipe image was successfully deleted!', 'success')
        db.session.commit()
        return 'success'

    flash('Oopss! It seems that you dont have the right to delete this image!', 'danger')
    return 'error'

@mod.route('/category/<int:category_id>/<slug>')
def category(category_id, slug):
    """Category recipes page.

    Displays a list of recipes for the provided category.

    Args:
        category_id: The category id for which recipes are shown
        slug: Category name slug. For SEO only
    """

    try:
        category = db.session.query(Category).filter_by(id=category_id).one()
        recipes = db.session.query(Recipe) \
            .filter_by(category_id=category_id) \
            .order_by(Recipe.title.asc()).all()
    except:
        flash('An error occurred, please try again later!')
        return redirect(url_for('general.index'))

    return render_template('recipes/by_category.html', recipes=recipes, category=category)

@mod.route('.json')
def json():
    """Recipes list in JSON format."""
    recipes = db.session.query(Recipe).order_by(Recipe.category_id.asc(), Recipe.title.asc())
    return jsonify(recipes=[recipe.to_json() for recipe in recipes])

@mod.route('.xml')
def xml():
    """Recipes list in XML format."""
    recipes = db.session.query(Recipe).order_by(Recipe.category_id.asc(), Recipe.title.asc())
    xml = unparse(dict(recipes=dict(recipe=[recipe.to_json() for recipe in recipes])))
    return Response(xml, mimetype='text/xml')
