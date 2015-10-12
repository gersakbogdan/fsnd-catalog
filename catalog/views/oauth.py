from flask import Blueprint, render_template, redirect, flash, url_for
from flask.ext.login import current_user, login_user, logout_user

from catalog.oauth import OAuthSignIn
from catalog.models.user import User
from catalog import db, lm

mod = Blueprint('oauth', __name__)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@mod.route('/authorize/<provider>/')
def authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('general.index'))

    return OAuthSignIn.get_provider(provider).authorize()

@mod.route('/callback/<provider>')
def callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('general.index'))

    social_id, username, email, picture = OAuthSignIn.get_provider(provider).callback()
    if social_id is None:
        flash('Authentication failed.', 'danger')
        return redirect(url_for('general.index'))

    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id, username, email, picture)
        db.session.add(user)
        db.session.commit()

    login_user(user, True)
    return redirect(url_for('general.index'))

@mod.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('general.index'))
