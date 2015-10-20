from xmltodict import unparse
from flask import Blueprint, render_template, flash, request
from flask import redirect, url_for, jsonify, Response
from flask.ext.login import current_user, login_required
from sqlalchemy.orm import exc

from catalog import db
from catalog.forms.category import CategoryForm
from catalog.models.category import Category
from catalog.helpers import upload_category_image, delete_category_image
from catalog.helpers import csrf_protect

mod = Blueprint('categories', __name__, url_prefix='/categories')


@mod.route('/')
def index():
    """Categories main index page.

    Displays the list of categories ordered by name.
    """

    categories = db.session.query(Category).order_by(Category.name).all()
    return render_template('categories/index.html', categories=categories)


@mod.route('/new/', methods=['GET', 'POST'])
@login_required
def new():
    """Create new category page.

    Displays the form to create a new category. If the form is successfully
    submitted an success message is shown.
    This page can be accessed only by logged in users.
    """

    form = CategoryForm()
    if request.method == 'GET':
        pass
    elif form.validate_on_submit():
        category = Category(form.name.data, form.description.data)

        db.session.add(category)
        db.session.flush()

        upload_category_image(form.image.data, category.id)

        db.session.commit()
        flash('Hooray! Category was successfully added!', 'success')
    else:
        print form.errors.items()
        flash('Oopss! There are some issues to fix here...', 'danger')
    return render_template('categories/new.html', form=form)


@mod.route('/<int:category_id>/edit/', methods=['GET', 'POST'])
@login_required
def edit(category_id):
    """Category edit page.

    Displays the form to edit a category.
    This page can be accessed only by logged in users.

    Args:
        category_id: The category id to be edit
    """

    try:
        category = db.session.query(Category).filter_by(id=category_id).one()
    except:
        flash('Oopss! Category does not exists!', 'danger')
        return redirect(url_for('categories.index'))

    form = CategoryForm(obj=category)
    if request.method == 'GET':
        pass
    elif form.validate_on_submit():
        category.name = form.name.data
        category.description = form.description.data
        if form.image.data and form.image.data.filename:
            upload_category_image(form.image.data, category.id)
        db.session.add(category)
        db.session.commit()
        flash('Hooray! Category was successfully added!', 'success')
    else:
        print form.errors.items()
        flash('Oopss! There are some issues to fix here...', 'danger')
    return render_template(
        'categories/edit.html', form=form, category_image=category.image_src
    )


@mod.route('/<int:category_id>/delete/', methods=['GET', 'POST'])
@login_required
def delete(category_id):
    """Delete category handler.

    Deletes the category from the database if exists. All the associated
    recipes and images will also be deleted.
    This page can be accessed only by logged in users and CSRF check runs
    for each delete.

    Args:
        category_id: The category id to be deleted
    """

    if request.method == 'GET':
        return redirect(url_for('categories.index'))
    elif current_user.is_admin:
        csrf_protect()  # csrf protection
        try:
            category = db.session.query(Category) \
                .filter_by(id=category_id) \
                .one()
            db.session.delete(category)
            flash(
                'Category "%s" successfully deleted' % category.name, 'success'
            )
            delete_category_image(category_id)
            db.session.commit()
        except exc.NoResultFound:
            flash('Category does not exists!', 'danger')
            return 'error'
        except:
            flash('An error occurred, please try again later!')
            return 'error'

        return 'success'

    flash('Oopss! You are not allowed to delete categories!', 'danger')
    return 'error'


@mod.route('.json')
def json():
    """Categories list in JSON format."""

    categories = db.session.query(Category).order_by(Category.name)
    return jsonify(categories=[category.to_dict() for category in categories])


@mod.route('.xml')
def xml():
    """Categories list in XML format."""

    categories = db.session.query(Category).order_by(Category.name)
    xml = unparse(
        dict(
            categories=dict(
                category=[category.to_dict() for category in categories]
            )
        )
    )
    return Response(xml, mimetype='text/xml')
