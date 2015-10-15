from flask.ext.wtf import Form
from flask.ext.wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import Required, Length, NumberRange

from catalog.models.category import Category

def categories():
    return Category.query.order_by(Category.name)

class RecipeForm(Form):
    """Basic form which allows to add or to edit a recipe."""

    category = QuerySelectField('category_id', query_factory=categories, get_label='name', allow_blank=True, blank_text=u'Choose category', validators=[Required()])
    title = StringField('title', validators=[Required(), Length(min=1, max=200)])
    description = TextAreaField('description', validators=[Required(), Length(min=1, max=500)])
    ingredients = TextAreaField('ingredients', validators=[Required(), Length(min=1, max=4000)])
    directions = TextAreaField('directions', validators=[Required(), Length(min=1, max=4000)])

    prep_time = IntegerField('prep_time', validators=[Required(),NumberRange(min=1,max=300)])
    cook_time = IntegerField('cook_time', validators=[Required(),NumberRange(min=1,max=300)])
    servings = IntegerField('servings', validators=[Required(),NumberRange(min=1,max=100)])

    image1 = FileField('image_1', validators=[FileAllowed(['jpeg', 'jpg', 'png'], 'Only images are allowed!')])
    image2 = FileField('image_2', validators=[FileAllowed(['jpeg', 'jpg', 'png'], 'Only images are allowed!')])
    image3 = FileField('image_3', validators=[FileAllowed(['jpeg', 'jpg', 'png'], 'Only images are allowed!')])
