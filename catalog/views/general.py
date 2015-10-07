from flask import Blueprint, render_template, redirect, url_for, g, session, flash
from catalog import app

mod = Blueprint('general', __name__)

@mod.route('/')
def index():
    return render_template('general/index.html')

@mod.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('general/login.html')

@mod.route('/logout/')
def logout():
    return redirect(url_for('general.index'))

@mod.route('/profile/')
def profile():
    return render_template('general/profile.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
