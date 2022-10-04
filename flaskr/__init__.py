import os
from flask import Flask, render_template, request

def create_app(test_config=None):
    # Create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')

    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # The routes to be defined

    @app.route("/", methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            # Get the submitted amount of recipes
            amountToGenerate = request.form['amountToGenerate']

            # TODO: Implement Flash messages if the input isn't correct

            # TODO: Print out the recipes
            print(f'{amountToGenerate} recepten gegenereerd')

            return render_template('index.html')
        else:
            return render_template('index.html')
    
    @app.route('/add-recipe', methods=['GET', 'POST'])
    def addRecipe():
        return render_template('addRecipe.html')

    @app.route('/all-recipes')
    def allRecipes():
        return render_template('allRecipes.html')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('pageNotFound.html'), 404

    from . import db
    db.init_app(app)

    return app

