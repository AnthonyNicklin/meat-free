from app import app
from flask import Flask, render_template, request, session, url_for, redirect, flash
from bson.objectid import ObjectId

from app import mongo


# --------------------------------------------------------------------- Login page
@app.route('/')
@app.route('/index')
def index():
    """ Landing page which displays login form if not already signed in  """

    if "username" in session:
        return redirect(url_for('recipes'))
    else:
        return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Login form function to sign in """

    users = mongo.db.user_accounts
    user = users.find_one({"username": request.form['username']})

    if user:
        session['username'] = request.form['username']
        name = user['first-name'].title()
        session['name'] = name
        return redirect(url_for('recipes'))
    else:
        flash("Username '{}' not found or invalid. Please try again or create an account by clicking on 'Sign Up'".format(request.form['username']))
        return redirect('index')


# --------------------------------------------------------------------- Sign Up
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    """ Sign up form """

    return render_template('sign_up.html', title="Sign Up")


@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    """ Logic to creates user and stores in collection called 'user_accounts' """

    users = mongo.db.user_accounts

    user_details = {
        "first-name": request.form["first-name"],
        "last-name": request.form["last-name"],
        "username": request.form["username"]
    }

    if request.method == "POST":
        if users.find_one({"username": user_details["username"]}) is None:
            users.insert_one(user_details)
            session['username'] = user_details['username']
            session['first-name'] = user_details['first-name']
            return redirect(url_for('recipes'))
        else:
            flash("'{}' has already been taken. Please try another username".format(user_details['username']))
            return redirect(url_for('sign_up'))

# --------------------------------------------------------------------- Logout
@app.route('/logout')
def logout():
    """ Function to log the user out by clearing the session """

    session.clear()
    return redirect(url_for('index'))

# --------------------------------------------------------------------- Recipes
@app.route('/add_recipe')
def add_recipe():
    """ Render template displaying form to add new recipe """

    return render_template('add_recipe.html', title='Add Recipe')


@app.route('/recipes')
def recipes():
    """ Render template displaying all recipes in a summarised view from 'recipes' collection """

    recipe = mongo.db.recipes.find()

    return render_template('recipes.html', title='Recipes', recipes=recipe)


@app.route('/insert_recipe', methods=["GET", "POST"])
def insert_recipe():
    """ Logic to insert new recipe into 'recipes' collection from add_recipe"""

    recipe = mongo.db.recipes

    if request.method == "POST":
        ingredients = request.form.getlist('ingredient')        # Collected data and store into arrays
        allergens = request.form.getlist('allergens')
        methods = request.form.getlist('method')

        recipe_details = {
            "name_of_recipe": request.form["name_of_recipe"],   # Dictionary storing all data collected
            "author": request.form["author"],
            "description": request.form["description"],
            "training_type": request.form['training_type'],
            "time_to_make": request.form['time_to_make'],
            "serves": request.form["serves"],
            "difficulty": request.form["difficulty"],
            "meal_time": request.form["meal_time"],
            "allergens": allergens,
            "ingredients": ingredients,
            "method": methods
        }
        recipe.insert_one(recipe_details)

        return redirect(url_for('recipes'))


@app.route('/recipe_detail/<recipe_id>')
def recipe_detail(recipe_id):
    """ Render template to display a recipe in detail """

    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})

    return render_template('recipe_detail.html', recipe=recipe)


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """ Render the edit_recipe page for the recipe to be updated """

    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})

    return render_template('edit_recipe.html', recipe=recipe)


@app.route('/update_recipe/<recipe_id>', methods=["GET", "POST"])
def update_recipe(recipe_id):
    """ Take the amended values from edit_recipe and update them into 'recipes' collection """

    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})

    # Get each item from the recipe and check if value has been changed. If changed update recipe.
    if request.form.get("name_of_recipe") != recipe["name_of_recipe"]:
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                    {"$set": {"name_of_recipe": request.form.get("name_of_recipe")}})

    if request.form.get("author") != recipe["author"]:
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                    {"$set": {"author": request.form.get("author")}})

    if request.form.get("description") != recipe["description"]:
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                {"$set": {"description": request.form.get("description")}})

    if request.form.get("time_to_make") != recipe["time_to_make"]:
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                {"$set": {"time_to_make": request.form.get("time_to_make")}})

    if request.form.get("training_type") is not None:
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                {"$set": {"training_type": request.form.get("training_type")}})

    if request.form.get("serves") != recipe["serves"]:
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                {"$set": {"serves": request.form.get("serves")}})

    if request.form.get("allergens") is not None:
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                {"$set": {"allergens": request.form.getlist("allergens")}})

    if request.form.get("difficulty") is not None:
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                {"$set": {"difficulty": request.form.get("difficulty")}})

    if request.form.get("meal_time") is not None:
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                {"$set": {"meal_time": request.form.get("meal_time")}})

    if request.form.get("ingredient") is not None:
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                {"$set": {"ingredient": request.form.getlist("ingredient")}})  # Not working. No detecting values.

    if request.form.get("method") is not None:
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                {"$set": {"method": request.form.getlist("method")}})

    return redirect(url_for('recipes'))


@app.route('/delete_recipe/<recipe_id>', methods=['GET', 'POST'])
def delete_recipe(recipe_id):
    """ Delete recipe """

    # Get the recipe to delete
    recipe_to_delete = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # Delete the recipe from the db
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})

    # Let the user know the recipe has been deleted
    flash("'{}' was successfully deleted.".format(recipe_to_delete['name_of_recipe'].title()))

    return redirect(url_for('recipes'))

# --------------------------------------------------------------------- Test page
@app.route('/test')
def test():
    """ Test page for styling remove before deploying! """

    return render_template('test.html')

# git remote add origin https://github.com/AnthonyNicklin/ms-3-mf.git