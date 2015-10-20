from flask import Blueprint, render_template, redirect, flash, url_for
from flask.ext.login import current_user, login_user, logout_user

from catalog.oauth import OAuthSignIn
from catalog.models.user import User
from catalog import db, lm

mod = Blueprint('oauth', __name__)


@lm.user_loader
def load_user(id):
    """Returns the logged in User model."""

    return User.query.get(int(id))


@mod.route('/authorize/<provider>/')
def authorize(provider):
    """Initiate authorization with the provider.

    If there is no logged in user this method initiate the authorization
    process with the provider received as parameter.
    Check OAuthSignIn class for more details about authorize implementation.

    Args:
        provider: The provider name: facebook, twitter, etc.
    """

    if not current_user.is_anonymous:
        return redirect(url_for('general.index'))

    return OAuthSignIn.get_provider(provider).authorize()


@mod.route('/callback/<provider>')
def callback(provider):
    """Verify authorization status.

    This method consist in the second step of authorization with the
    thirth-party provider. If authorization succeed a new user is added to
    the database if doesn't exists yet.

    Args:
        provider: The provider name: facebook, twitter, etc.
    """

    if not current_user.is_anonymous:
        return redirect(url_for('general.index'))

    social_id, username, email, picture = OAuthSignIn.get_provider(provider) \
        .callback()

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
    """Logout user and display index page."""

    logout_user()
    return redirect(url_for('general.index'))
