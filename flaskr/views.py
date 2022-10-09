from flask import (
    Blueprint, redirect, render_template, request, session, url_for, flash
)

import sqlite3

from flaskr.db import get_db

from .auth import login_required

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        db = get_db()
        error = None

        # Get the submitted amount of recipes
        amountToGenerate = request.form['amountToGenerate']

        if int(amountToGenerate) < 1 or int(amountToGenerate) > 5:
            error = "Vul een nummer van 1 tot 5 in."
            flash(error)
            return render_template('index.html')

        # TODO: Implement Flash messages if the input isn't correct
        query = db.execute(
            'SELECT * FROM recipes ORDER BY RANDOM() LIMIT ?;',
            (amountToGenerate)
        )

        return render_template('index-generated.html', query=query)
    else:
        return render_template('index.html')

@views.route('/add-recipe', methods=['GET', 'POST'])
@login_required
def addRecipe():
    if request.method == 'POST':
        recipeName = request.form['recipeName']
        recipeRating = request.form['recipeRating']
        url = request.form['url']
        recipeAuthor = request.form['recipeAuthor']
        recipeRating = request.form['recipeRating']
        submittedBy = request.form['submittedBy']

        error = None
        db = get_db()

        if not recipeName:
            error = 'Voeg de naam van het recept toe.'
        if not recipeRating:
            error = 'Geef een rating aan het recept.'
        if int(recipeRating) < 1 or int(recipeRating) > 5:
            error = 'Geef een rating tussen 1 en 5.'
        if not url:
            error = 'Voeg een geldige url van het recept toe.'
        if not recipeAuthor:
            error = 'Voeg een geldige auteur toe.'

        if error is None:
            try:
                db.execute(
                    'INSERT INTO recipes (submitted_by, name, author, rating, url) VALUES (?, ?, ?, ?, ?)',
                    (submittedBy, recipeName, recipeAuthor, recipeRating, url)
                )
                db.commit()
            except db.IntegrityError:
                error = "Recipe is already registered."           
            else:
                flash(f'{recipeName} werd succesvol toegevoegd aan de database!')
                return redirect(url_for('views.addRecipe'))


        flash(error)
        return render_template('addRecipe.html')



    else:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM user;')
        query = cursor.fetchall()

        for row in query:
            print(row['id'])

        return render_template('addRecipe.html', query=query)

@views.route('/all-recipes')
@login_required
def allRecipes():
    db = get_db()

    query = db.execute(
        'SELECT * FROM recipes;'
    )

    return render_template('allRecipes.html', query=query)

@views.errorhandler(404)
def page_not_found(error):
    return render_template('pageNotFound.html'), 404