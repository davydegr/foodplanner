from flask import Flask, request, render_template, url_for, redirect, abort, session

app = Flask(__name__)

# If you refer to one of these urls, use URL Building
'''
    url_for(index) 
    -> This takes the function name as an argument
    -> returns the actual url so you don't have to hardcode
'''

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

