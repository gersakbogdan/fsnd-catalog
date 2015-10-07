from flask import Blueprint, render_template, redirect, url_for, g, session, flash
from catalog import app

mod = Blueprint('categories', __name__, url_prefix='/categories')

@mod.route('/')
def index():
    return render_template('categories/index.html')

@mod.route('/new/', methods=['GET', 'POST'])
def new():
    return render_template('categories/new.html')

@mod.route('/edit/<int:id>/', methods=['GET', 'POST'])
def edit(id):
    return render_template('categories/edit.html', id=id)

@mod.route('/delete/<int:id>/', methods=['GET', 'POST'])
def delete(id):
    return render_template('categories/delete.html', id=id)
