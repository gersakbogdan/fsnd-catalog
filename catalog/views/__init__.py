from catalog import app
import general, categories, recipes, oauth

app.register_blueprint(general.mod)
app.register_blueprint(categories.mod)
app.register_blueprint(recipes.mod)
app.register_blueprint(oauth.mod)
