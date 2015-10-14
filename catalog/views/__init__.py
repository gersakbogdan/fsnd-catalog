from catalog import app

import catalog.views.general
import catalog.views.categories
import catalog.views.recipes
import catalog.views.oauth

# Register all necessary blueprints
# Blueprints reference: http://flask.pocoo.org/docs/0.10/blueprints/
app.register_blueprint(general.mod)
app.register_blueprint(categories.mod)
app.register_blueprint(recipes.mod)
app.register_blueprint(oauth.mod)
