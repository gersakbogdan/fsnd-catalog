import os
import re
import uuid

from unicodedata import normalize
from PIL import Image, ImageOps
from flask import request, session, abort

from catalog import app

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-'):
    """Generates slug from string."""

    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))


def formated_time(minutes):
    """Convert integer to hours and minutes format."""

    h, m = divmod(minutes, 60)
    if h > 0 and m > 0:
        return '%d h %d mins' % (h, m)
    elif h > 0:
        return '%d h' % h
    return '%d mins' % m


def upload_recipe_image(imagedata, size=(700, 450)):
    """Save and resize recipe image."""

    save_path = os.path.join(app.config['UPLOAD_FOLDER'], 'recipes')
    return upload_image(imagedata, save_path, size)


def upload_category_image(imagedata, category_id):
    """Save and resize to (128,128) the uploaded category image."""

    filename = '%s.%s' % (category_id, 'png')
    file_path = os.path.join(
        app.config['UPLOAD_FOLDER'], 'categories', filename
    )

    image_file = ImageOps.fit(
        Image.open(imagedata), (128, 128), Image.ANTIALIAS
    )
    image_file.save(file_path)


def upload_image(imagedata, save_path, size):
    """General save upload image meethod."""

    # save uploaded file
    ext = imagedata.filename.split('.')[-1]
    # generate a safe name for image
    filename = '%s.%s' % (uuid.uuid4(), ext)
    file_path = os.path.join(save_path, filename)
    # change size
    image_file = ImageOps.fit(Image.open(imagedata), size, Image.ANTIALIAS)
    image_file.save(file_path)

    return filename


def delete_category_image(category_id):
    try:
        filename = '%s.%s' % (category_id, 'png')
        file_path = os.path.join(
            app.config['UPLOAD_FOLDER'], 'categories', filename
        )
        os.remove(file_path)
    except OSError:
        pass


def delete_recipe_image(filename):
    try:
        file_path = os.path.join(
            app.config['UPLOAD_FOLDER'], 'recipes', filename
        )
        os.remove(file_path)
    except OSError:
        pass


def csrf_protect():
    """Check request against CSRF.

    This method compares session token with request token and if there
    is no match 403 error is returned.
    """

    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or str(token) != str(request.form.get('_csrf_token')):
            abort(403)


def generate_csrf_token():
    """Generates and return CSRF token."""

    if '_csrf_token' not in session:
        session['_csrf_token'] = uuid.uuid4()
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token
