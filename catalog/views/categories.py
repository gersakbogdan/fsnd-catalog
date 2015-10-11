from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask.ext.login import current_user, login_required

from catalog import db
from catalog.forms.category import CategoryForm
from catalog.models.category import Category
from catalog.helpers import upload_category_image, delete_category_image

mod = Blueprint('categories', __name__, url_prefix='/categories')

@mod.route('/')
def index():
    categories = db.session.query(Category).order_by(Category.name)
    return render_template('categories/index.html', categories=categories)

@mod.route('/new/', methods=['GET', 'POST'])
@login_required
def new():
    form = CategoryForm()
    if request.method == 'GET':
        pass
    elif form.validate_on_submit():
        category = Category(form.name.data, form.description.data)

        db.session.add(category)
        db.session.flush()

        upload_category_image(form.image.data, category.id)

        db.session.commit()
        flash(('success', 'Hooray! Category was successfully added!'))
    else:
        print form.errors.items()
        flash(('danger', 'Oopss! There are some issues to fix here...'))
    return render_template('categories/new.html', form=form)

@mod.route('/<int:category_id>/edit/', methods=['GET', 'POST'])
def edit(category_id):
    category = db.session.query(Category).filter_by(id=category_id).one()
    form = CategoryForm(obj=category)
    if request.method == 'GET':
        pass
    elif form.validate_on_submit():
        category.name = form.name.data
        category.description = form.description.data
        upload_category_image(form.image.data, category.id)
        db.session.add(category)
        db.session.commit()
        flash(('success', 'Hooray! Category was successfully added!'))
    else:
        print form.errors.items()
        flash(('danger', 'Oopss! There are some issues to fix here...'))
    return render_template('categories/edit.html', form=form, category_image=category.image_src)

@mod.route('/<int:category_id>/delete/', methods=['GET', 'POST'])
@login_required
def delete(category_id):
    if request.method == 'GET':
        return redirect(url_for('categories.index'))
    elif current_user.is_admin:
        category = db.session.query(Category).filter_by(id=category_id).one()
        db.session.delete(category)
        flash(('success', 'Category "%s" successfully deleted' % category.name))
        delete_category_image(category_id)
        db.session.commit()
        return 'success'

    flash(('danger', 'Oopss! It seems that you dont have the right to delete categories!'))
    return 'error'
