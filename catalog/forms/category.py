from flask.ext.wtf import Form
from flask.ext.wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField
from wtforms.validators import Required, Length

class CategoryForm(Form):
    name = StringField('name', validators=[Required(), Length(min=1, max=20)])
    description = TextAreaField('description', validators=[Required(), Length(min=1, max=500)])
    image = FileField('image', validators=[FileAllowed(['jpeg', 'jpg', 'png'], 'Only images are allowed!')])
