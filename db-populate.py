#!flask/bin/python
# -*- coding: utf-8 -*-

from catalog import db
from catalog.models.user import User
from catalog.models.category import Category
from catalog.models.recipe import Recipe, RecipeImage

user = User('facebook$10206593265223852', 'John Doe', 'example@email.do', None)
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
meat = Category(
    'Meat & Poultry',
    'Top recipes for beef, chicken, pork, and more. \
    See classic recipes or find something new.'
)
db.session.add(meat)
sea = Category(
    'Seafood',
    'Top recipes for fish, shellfish, and hearty chowder. \
    See easy ways to make seafood part of your low-cal diet.')
db.session.add(sea)

db.session.commit()

appetizer_recipe_1 = Recipe(
    user,
    appetizer,
    u'Blue Cheese Crostini with Balsamic-Roasted Grapes',
    u'Keep this recipe in your back pocket to use as your go-to for \
    last-minute company. You can also serve the grapes with chicken or pork \
    in lieu of a sauce. Or toss them in salads.',
    u'2 cups halved seedless red grapes\r\n2 tablespoons balsamic vinegar\r\n\
    1 1/2 tablespoons minced shallot\
    2 teaspoons olive oil\r\n1/2 teaspoon light brown sugar \r\n\
    1/4 teaspoon kosher salt\r\n\
    1 (12-oz.) French bread baguette, cut into 15 to 20 (1/2-inch-thick) \
    slices\
    3 tablespoons butter, softened\r\n2 ounces crumbled blue cheese, \
    softened\r\n\
    1/3 cup chopped toasted pecans\
    Garnish: chopped fresh thyme',
    u'Preheat oven to 425F. Toss together first 6 ingredients.\r\n\
    Arrange grapes in a single layer in a small roasting pan;\r\n\
    bake 15 to 20 minutes or until grapes wilt and liquid forms a \
    thin syrup.\r\n\
    Remove from oven.2. Increase oven temperature to broil with oven rack 7 \
    inches from heat.\r\n\
    Arrange bread slices in a single layer on a baking sheet. Stir together \
    butter and cheese, and\r\n\
    spread evenly over bread slices. Broil 2 to 3 minutes or until browned \
    and bubbly.\r\n\
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
    u'Phyllo-Wrapped Asparagus with Prosciutto is an appetizer worthy of a \
    special occasion. Simply roll up prosciutto and asparagus in phyllo dough \
    and bake. The results are a crunchy, easy appetizer all will enjoy. \
    You can also chop the prosciutto and sprinkle it on the phyllo.',

    u'3 ounces thinly sliced prosciutto, cut into 30 long, thin strips\r\n\
     30 asparagus spears, trimmed\r\n\
     10 (14 x 9-inch) sheets frozen phyllo dough, thawed\r\n\
     Cooking spray',

    u'Preheat oven to 450C\r\n\
     Wrap 1 prosciutto strip around each asparagus spear, barber \
     polestyle.\r\n\
     Place 1 phyllo sheet on a work surface \
     (cover remaining phyllo to prevent drying);\r\n\
     coat phyllo with cooking spray. Cut crosswise into thirds to form \
     3 (4 1/2 x 9inch) rectangles.\r\n\
     Arrange 1 asparagus spear across 1 short end of each rectangle; \
     roll up jelly-roll fashion.\r\n\
     Arrange rolls on a baking sheet; coat rolls with cooking spray. \
     Repeat procedure with remaining phyllo,\r\n\
     asparagus, and cooking spray. Bake at 450C for 10 minutes or until \
     phyllo is golden and crisp.\r\n\
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
    u'MOINK. Well this is a crazy word isn\'t it? This word has been \
    circulating around the internet BBQ world for quite some time. \
    The general idea is that it came from "moo" and "oink" put together \
    since you\'re using beef meatballs and pork bacon. MOINK balls are bacon\
     wrapped meatballs that are smoked for about 1.5 hours. They are dusted \
     with BBQ dry rub and brushed with BBQ sauce. I decided to give it a try. \
     It\'s a really simple and tasty appetizer.',
    u'Bag of meatballs from the frozen food section (not Italian seasoned); \
    thawed\r\n\
    Any BBQ dry rub you have in your pantry\r\n\
    1 pack of bacon\r\n\
    Toothpicks\r\n\
    Any BBQ sauce you have lying around',
    u'So go ahead and cut your bacon in half (see above photo) and get your \
    meatballs out. Look in the pantry for that leftover BBQ dry rub and get \
    that out too.\r\n\
    Take each thawed meatball and wrap it with half a piece of bacon. \
    Stick a toothpick in to keep it secure. These meatballs were pretty \
    small so a half a slice of bacon was more than enough. Too much bacon \
    would actually not work well here, so stick with a half piece. \
    Once all of the meatballs are wrapped with bacon and impaled with a \
    toothpick shake the BBQ dry rub all over. This is why I don\'t use \
    Italian flavored meatballs because I suspect the BBQ dry rub and Italian \
    seasonings don\'t go too well together.\r\n\
    The assembled MOINK balls can sit in the fridge as long as you like. \
    I made these in the morning and then smoked them in the afternoon.',
    30,
    90,
    8
)
db.session.add(bbq_recipe_1)

breakfast_recipe_1 = Recipe(
    user,
    breakfast,
    u'Baked eggs in popped beans',
    u'Mighty cannellini beans are a great source of protein, high in fibre, \
    and contain vitamin C as well as magnesium, a mineral that helps our \
    muscles to function properly',
    u'250g mixed-colour ripe cherry tomatoes\r\n\
    1/2 a lemon\r\n\
    extra virgin olive oil\r\n\
    4 sprigs of fresh basil\r\n\
    1x400g tin of cannellini beans\r\n\
    1 good pinch of fennel seeds\r\n\
    2 large free-range eggs\r\n\
    2 slices of seeded wholemeal bread\r\n\
    2 heaped teaspoons ricotta cheese\r\n\
    thick balsamic vinegar, optional\r\n\
    hot chilli sauce, optional',
    u'Halve the tomatoes, place in a bowl and toss with the lemon juice, \
    1 tablespoon of oil and a pinch of sea salt. Pick, tear and toss in the \
    basil leaves (reserving the smaller ones for garnish), then leave aside \
    to macerate for a few minutes.\r\n\
    Meanwhile, place a large non-stick frying pan on a high heat. Drain the \
    beans and put into the hot pan with the fennel seeds and a pinch of black \
    pepper. Leave for 5 minutes, shaking occasionally – you want them to char \
    and pop open, bursting their skins. Pour the macerated tomatoes into the \
    pan with 100ml of water, season, then leave to bubble away vigorously for \
    1 minute. Crack in an egg on each side, then cover with a lid, plate or \
    tin foil, reduce to a medium-low heat and slow-cook for 3 to 4 minutes for\
    nice soft eggs, or longer if you prefer. Meanwhile, toast the bread.\r\n\
    Divide the ricotta and spread over the two pieces of hot toast, then serve\
     on the side of the baked eggs in beans. Sprinkle the reserved baby basil\
      leaves over the top and tuck right in. Nice finished with a drizzle of \
      balsamic vinegar and/or a drizzle of hot chilli sauce. Delicious.',
    10,
    20,
    2
)
db.session.add(breakfast_recipe_1)

drinks_recipe_1 = Recipe(
    user,
    drinks,
    u'Berry & rosemary juniper gin fizz',
    u'Nullam rutrum viverra metus ac fermentum. \
    Maecenas condimentum a odio eu tempor. Duis auctor commodo feugiat. \
    Praesent non posuere purus. Donec eget massa ultrices est aliquet \
    facilisis. Sed sed gravida magna. Nunc eu pharetra urna. \
    Pellentesque facilisis mattis enim quis placerat.',
    u'Aenean dapibus urna pellentesque quam faucibus finibus.\r\n\
    Praesent vitae ligula et felis tempus malesuada.\r\n\
    Quisque quis ligula quis augue laoreet sollicitudin in ut ligula.\r\n\
    Integer ut mi rhoncus metus ultrices molestie ut ut arcu.\r\n\
    Morbi volutpat tortor sit amet dapibus semper.\r\n\
    Donec at felis sit amet magna consequat volutpat.',
    u'Duis porta maximus interdum. Aliquam non erat leo.\r\n\
    Donec id tempus ipsum, et euismod tortor. Pellentesque sagittis \
    ac erat non mattis.\r\n\
    Praesent a enim urna. Mauris porta tortor quis ligula blandit, \
    nec dapibus nisl convallis.\r\n\
    Quisque placerat metus dolor, et sagittis dui ornare at. Duis ac velit \
    vestibulum, vestibulum augue quis, aliquam nunc.\r\n\
    Morbi eget sem ut arcu vestibulum faucibus et sed massa.',
    35,
    25,
    9
)
db.session.add(drinks_recipe_1)

dinner_recipe_1 = Recipe(
    user,
    dinner,
    u'Whole roasted pheasant',
    u'Nullam rutrum viverra metus ac fermentum. \
    Maecenas condimentum a odio eu tempor. Duis auctor commodo feugiat. \
    Praesent non posuere purus. Donec eget massa ultrices est aliquet \
    facilisis. Sed sed gravida magna. Nunc eu pharetra urna. \
    Pellentesque facilisis mattis enim quis placerat.',
    u'Aenean dapibus urna pellentesque quam faucibus finibus.\r\n\
    Praesent vitae ligula et felis tempus malesuada.\r\n\
    Quisque quis ligula quis augue laoreet sollicitudin in ut ligula.\r\n\
    Integer ut mi rhoncus metus ultrices molestie ut ut arcu.\r\n\
    Morbi volutpat tortor sit amet dapibus semper.\r\n\
    Donec at felis sit amet magna consequat volutpat.',
    u'Duis porta maximus interdum. Aliquam non erat leo.\r\n\
    Donec id tempus ipsum, et euismod tortor. Pellentesque sagittis \
    ac erat non mattis.\r\n\
    Praesent a enim urna. Mauris porta tortor quis ligula blandit, \
    nec dapibus nisl convallis.\r\n\
    Quisque placerat metus dolor, et sagittis dui ornare at. Duis ac velit \
    vestibulum, vestibulum augue quis, aliquam nunc.\r\n\
    Morbi eget sem ut arcu vestibulum faucibus et sed massa.',
    55,
    85,
    4
)
db.session.add(dinner_recipe_1)

fruits_recipe_1 = Recipe(
    user,
    fruits,
    u'Classic ratatouille',
    u'Nullam rutrum viverra metus ac fermentum. \
    Maecenas condimentum a odio eu tempor. Duis auctor commodo feugiat. \
    Praesent non posuere purus. Donec eget massa ultrices est aliquet \
    facilisis. Sed sed gravida magna. Nunc eu pharetra urna. \
    Pellentesque facilisis mattis enim quis placerat.',
    u'Aenean dapibus urna pellentesque quam faucibus finibus.\r\n\
    Praesent vitae ligula et felis tempus malesuada.\r\n\
    Quisque quis ligula quis augue laoreet sollicitudin in ut ligula.\r\n\
    Integer ut mi rhoncus metus ultrices molestie ut ut arcu.\r\n\
    Morbi volutpat tortor sit amet dapibus semper.\r\n\
    Donec at felis sit amet magna consequat volutpat.',
    u'Duis porta maximus interdum. Aliquam non erat leo.\r\n\
    Donec id tempus ipsum, et euismod tortor. Pellentesque sagittis \
    ac erat non mattis.\r\n\
    Praesent a enim urna. Mauris porta tortor quis ligula blandit, \
    nec dapibus nisl convallis.\r\n\
    Quisque placerat metus dolor, et sagittis dui ornare at. Duis ac velit \
    vestibulum, vestibulum augue quis, aliquam nunc.\r\n\
    Morbi eget sem ut arcu vestibulum faucibus et sed massa.',
    35,
    25,
    4
)
db.session.add(fruits_recipe_1)

sea_recipe_1 = Recipe(
    user,
    sea,
    u'Prawn panzanella',
    u'Nullam rutrum viverra metus ac fermentum. \
    Maecenas condimentum a odio eu tempor. Duis auctor commodo feugiat. \
    Praesent non posuere purus. Donec eget massa ultrices est aliquet \
    facilisis. Sed sed gravida magna. Nunc eu pharetra urna. \
    Pellentesque facilisis mattis enim quis placerat.',
    u'Aenean dapibus urna pellentesque quam faucibus finibus.\r\n\
    Praesent vitae ligula et felis tempus malesuada.\r\n\
    Quisque quis ligula quis augue laoreet sollicitudin in ut ligula.\r\n\
    Integer ut mi rhoncus metus ultrices molestie ut ut arcu.\r\n\
    Morbi volutpat tortor sit amet dapibus semper.\r\n\
    Donec at felis sit amet magna consequat volutpat.',
    u'Duis porta maximus interdum. Aliquam non erat leo.\r\n\
    Donec id tempus ipsum, et euismod tortor. Pellentesque sagittis \
    ac erat non mattis.\r\n\
    Praesent a enim urna. Mauris porta tortor quis ligula blandit, \
    nec dapibus nisl convallis.\r\n\
    Quisque placerat metus dolor, et sagittis dui ornare at. Duis ac velit \
    vestibulum, vestibulum augue quis, aliquam nunc.\r\n\
    Morbi eget sem ut arcu vestibulum faucibus et sed massa.',
    95,
    55,
    4
)
db.session.add(sea_recipe_1)

# save changes
db.session.commit()
