import os, re, uuid

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
    h, m = divmod(minutes, 60)
    if h > 0 and m > 0:
        return '%d h %d mins' % (h, m)
    elif h > 0:
        return '%d h' % h
    return '%d mins' % m

def upload_recipe_image(imagedata, size=(700, 450)):
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], 'recipes')

    filename = upload_image(imagedata, save_path, size)
    if filename:
        thumb_path = os.path.join(save_path, 'thumb')
        upload_image(imagedata, thumb_path, (128, 128))

    return filename

def upload_category_image(imagedata, category_id):
    filename = '%s.%s' % (category_id, 'png')
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'categories', filename)

    image_file = ImageOps.fit(Image.open(imagedata), (128, 128), Image.ANTIALIAS)
    image_file.save(file_path)

def upload_image(imagedata, save_path, size):
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
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'categories', filename)
        os.remove(file_path)
    except OSError:
        pass

def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        print token, request.form.get('_csrf_token')
        if not token or str(token) != str(request.form.get('_csrf_token')):
            abort(403)

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = uuid.uuid4()
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token
