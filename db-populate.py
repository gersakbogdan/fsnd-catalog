#!flask/bin/python
# -*- coding: utf-8 -*-
from catalog import db
from catalog.models.user import User
from catalog.models.category import Category
from catalog.models.recipe import Recipe, RecipeImage

user = User('facebook$10206593265223852', 'Bogdan Gersak', 'bogdan@gersak.ro', None)
db.session.add(user)
appetizer = Category('Appetizer', 'Appetizers and Snacks')
db.session.add(appetizer)
bbq = Category('BBQ & Grilling', 'BBQ and Grilling')
db.session.add(bbq)
dessert = Category('Desserts', 'Sweets, Desserts')
db.session.add(dessert)
breakfast = Category('Breakfast', 'Breakfast and Brunch')
db.session.add(breakfast)
drinks = Category('Drinks', 'Drinks')
db.session.add(drinks)
dinner = Category('Dinner', 'Dinner')
db.session.add(dinner)
fruits = Category('Fruits & Vegetables', 'Fruits, Vegetables and Other')
db.session.add(fruits)
healthy = Category('Healthy Recipes', 'Healthy Food')
db.session.add(healthy)
lunch = Category('Lunch Recipes', 'Lunch recipes')
db.session.add(lunch)
meat = Category('Meat & Poultry', 'Top recipes for beef, chicken, pork, and more. See classic recipes or find something new.')
db.session.add(meat)
sea = Category('Seafood', 'Top recipes for fish, shellfish, and hearty chowder. See easy ways to make seafood part of your low-cal diet.')
db.session.add(sea)

db.session.commit()

appetizer_recipe_1 = Recipe(
    user,
    appetizer,
    u'Blue Cheese Crostini with Balsamic-Roasted Grapes',
    u'Keep this recipe in your back pocket to use as your go-to for last-minute company. You can also serve the grapes with chicken or pork in lieu of a sauce. Or toss them in salads.',
    u'2 cups halved seedless red grapes\r\n2 tablespoons balsamic vinegar\r\n1 1/2 tablespoons minced shallot\
    2 teaspoons olive oil\r\n1/2 teaspoon light brown sugar \r\n1/4 teaspoon kosher salt\
    1 (12-oz.) French bread baguette, cut into 15 to 20 (1/2-inch-thick) slices\
    3 tablespoons butter, softened\r\n2 ounces crumbled blue cheese, softened\r\n1/3 cup chopped toasted pecans\
    Garnish: chopped fresh thyme',
    u'Preheat oven to 425F. Toss together first 6 ingredients.\
    Arrange grapes in a single layer in a small roasting pan; \
    bake 15 to 20 minutes or until grapes wilt and liquid forms a thin syrup. \
    Remove from oven.2. Increase oven temperature to broil with oven rack 7 inches from heat. \
    Arrange bread slices in a single layer on a baking sheet. Stir together butter and cheese, and \
    spread evenly over bread slices. Broil 2 to 3 minutes or until browned and bubbly. \
    Spoon grape mixture over toasted bread, and sprinkle with pecans.',
    20,
    15,
    5
)
db.session.add(appetizer_recipe_1)

appetizer_recipe_2 = Recipe(
    user,
    appetizer,
    u'Phyllo-Wrapped Asparagus with Prosciutto',
    u'Phyllo-Wrapped Asparagus with Prosciutto is an appetizer worthy of a special occasion. Simply roll up prosciutto and asparagus in phyllo dough and bake. The results are a crunchy, easy appetizer all will enjoy. You can also chop the prosciutto and sprinkle it on the phyllo.',

    u'3 ounces thinly sliced prosciutto, cut into 30 long, thin strips\
     30 asparagus spears, trimmed\
     10 (14 x 9-inch) sheets frozen phyllo dough, thawed\
     Cooking spray',

    u'Preheat oven to 450C \
     Wrap 1 prosciutto strip around each asparagus spear, barber polestyle. \
     Place 1 phyllo sheet on a work surface (cover remaining phyllo to prevent drying); \
     coat phyllo with cooking spray. Cut crosswise into thirds to form 3 (4 1/2 x 9inch) rectangles. \
     Arrange 1 asparagus spear across 1 short end of each rectangle; roll up jelly-roll fashion. \
     Arrange rolls on a baking sheet; coat rolls with cooking spray. Repeat procedure with remaining phyllo, \
     asparagus, and cooking spray. Bake at 450C for 10 minutes or until phyllo is golden and crisp. \
     Serve warm or at room temperature.',
    20,
    25,
    8
)
db.session.add(appetizer_recipe_2)

bbq_recipe_1 = Recipe(
    user,
    bbq,
    u'Moink Balls - Smoked Bacon Wrapped Meatballs',
    u'MOINK. Well this is a crazy word isn\'t it? This word has been circulating around the internet BBQ world for quite some time. The general idea is that it came from "moo" and "oink" put together since you\'re using beef meatballs and pork bacon. MOINK balls are bacon wrapped meatballs that are smoked for about 1.5 hours. They are dusted with BBQ dry rub and brushed with BBQ sauce. I decided to give it a try. It\'s a really simple and tasty appetizer.',
    u'Bag of meatballs from the frozen food section (not Italian seasoned); thawed\r\n\
    Any BBQ dry rub you have in your pantry\r\n\
    1 pack of bacon\r\n\
    Toothpicks\r\n\
    Any BBQ sauce you have lying around',
    u'So go ahead and cut your bacon in half (see above photo) and get your meatballs out. Look in the pantry for that leftover BBQ dry rub and get that out too.\r\n\
    Take each thawed meatball and wrap it with half a piece of bacon. Stick a toothpick in to keep it secure. These meatballs were pretty small so a half a slice of bacon was more than enough. Too much bacon would actually not work well here, so stick with a half piece. Once all of the meatballs are wrapped with bacon and impaled with a toothpick shake the BBQ dry rub all over. This is why I don\'t use Italian flavored meatballs because I suspect the BBQ dry rub and Italian seasonings don\'t go too well together.\r\n\
    The assembled MOINK balls can sit in the fridge as long as you like. I made these in the morning and then smoked them in the afternoon.',
    30,
    90,
    8
)
db.session.add(bbq_recipe_1)
# save changes
db.session.commit()
