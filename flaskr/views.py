from flask import (
    Blueprint, redirect, render_template, request, session, url_for
)

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
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

@views.route('/add-recipe', methods=['GET', 'POST'])
def addRecipe():
    return render_template('addRecipe.html')

@views.route('/all-recipes')
def allRecipes():
    return render_template('allRecipes.html')

@views.errorhandler(404)
def page_not_found(error):
    return render_template('pageNotFound.html'), 404