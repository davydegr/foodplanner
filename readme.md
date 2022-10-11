# Foodplanner app

#### Video demo: https://youtu.be/M18rATPtYdw
#### Description:

This project is purely personal. Scraping other people's websites is purely for my own use. This will not be commercialized unless accepted by the rightful authors of the recipes.

As a food blogger, I have tons of recipes on my website (https://opmijntalloor.be). However, it sometimes still is a struggle to come up with what we actually want to eat.

* The user first has to login to truly access the app. If there is no user account, you can create one with the register button.
* This app has a database with recipes (currently some of my recipes). The whole database can currently be viewed under 'all recipes'
* The main part of this app is the index page (/). Here, the user can enter a number and the app will automatically and randomly select that amount of recipes. Therefore the user is able to always get recipes who otherwise might be left untouched because they're on the 10th page of our recipe section on our own website.
* If the user wants to add a recipe to the database, it is possible via /add-recipe, also accessible via the main menu

##### Files
* The application is built with Flask as seen in the CS50 course
* The application is built on the official Flask tutorial found in the documentation
* The application is mainly built with a basic styling from Bootstrap

* The whole app is situated in the "flaskr" folder
* The database is situated in the "instance" folder
* The installed packages are stored in requirements.txt
* A virtual environment was used to make sure the right packages are always installed
* All files have been managed with git and automatically added to my Github account:
https://github.com/davydegr/foodplanner

* auth.py manages all the authentication
* db.py manages commands used to access the database
* views.py manages all the views of the web app except for the authentication




## Upcoming functionalities
These functionalities are not yet implemented but are being worked on.

All upcoming functionalities are documented and kept track off in this Trello board: 
https://trello.com/invite/b/WyMtALeT/0c5871a9f5b6ab7fc06001a1b4574079/foodplanner

* Scrape my own website (opmijntalloor.be) and automatically insert our recipes into the database
* Write a script to scrape other foodbloggers' website and automatically insert the recipes into the database
* Let users save favourites in a separate menu
* Add a new table with all the recipe authors