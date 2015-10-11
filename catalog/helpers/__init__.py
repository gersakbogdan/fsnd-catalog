import os, re, uuid
from catalog import app
from PIL import Image, ImageOps
from unicodedata import normalize

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

def slugify(text, delim=u'-'):
    """Generates slug from string."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))

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
