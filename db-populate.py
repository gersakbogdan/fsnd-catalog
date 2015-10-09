#!flask/bin/python
from catalog import db
from catalog.models.category import Category

dessert = Category('Dessert')
chicken = Category('Chicken')
main_dish = Category('Main Dish')
appetizer = Category('Appetizer')

db.session.add(dessert)
db.session.add(chicken)
db.session.add(main_dish)
db.session.add(appetizer)
db.session.commit()
