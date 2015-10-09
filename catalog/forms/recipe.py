from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import Required, Length, NumberRange

from catalog.models.category import Category

def categories():
    return Category.query.order_by(Category.name)

class RecipeForm(Form):
    category = QuerySelectField('category_id', query_factory=categories, get_label='name', allow_blank=True, blank_text=u'Choose category', validators=[Required()])
    title = StringField('title', validators=[Required()])
    description = TextAreaField('description', validators=[Length(min=0, max=250)])
    ingredients = TextAreaField('ingredients', validators=[Length(min=0, max=999)])
    directions = TextAreaField('directions', validators=[Length(min=0, max=999)])

    prep_time = IntegerField('prep_time', validators=[Required(),NumberRange(min=1,max=300)])
    cook_time = IntegerField('cook_time', validators=[Required(),NumberRange(min=1,max=300)])
    servings = IntegerField('servings', validators=[Required(),NumberRange(min=1,max=100)])
