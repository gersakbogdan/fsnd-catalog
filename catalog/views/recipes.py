from flask import Blueprint, render_template, redirect, url_for, g, session, flash
from catalog import app

mod = Blueprint('recipes', __name__, url_prefix='/recipes')

@mod.route('/')
def index():
    return render_template('recipes/index.html')

@mod.route('/new/', methods=['GET', 'POST'])
def new():
    return render_template('recipes/new.html')

@mod.route('/edit/<int:id>/', methods=['GET', 'POST'])
def edit(id):
    return render_template('recipes/edit.html', id=id)

@mod.route('/delete/<int:id>/', methods=['GET', 'POST'])
def delete(id):
    return render_template('recipes/delete.html', id=id)
