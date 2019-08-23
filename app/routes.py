import os
from pygal import Pie, Bar
from bson.objectid import ObjectId

from flask import render_template, request, session, url_for, redirect, flash

from app import app, mongo


# --------------------------------------------------------------------- Decorators
def login_required(func):
    """ Check if the user has logged in """

    def wrapper(**kwargs):
        if not session.get('name'):
            flash('Please log in to access this website.')
            return render_template('index.html')
        else:
            return func(**kwargs)
    return wrapper

# --------------------------------------------------------------------- Login page
@app.route('/')
@app.route('/index')
def index():
    """ Landing page which displays login form if not already signed in  """

    if "username" in session:
        return render_template('get_types.html')
    else:
        return render_template('index.html')

# --------------------------------------------------------------------- Login function
@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Login form function to sign in """

    users = mongo.db.user_accounts
    user = users.find_one({"username": request.form['username']})

    if user:
        session['username'] = request.form['username']
        name = user['first-name'].title()
        session['name'] = name
        return render_template('get_types.html')
    else:
        flash("Username '{}' not found or invalid. "
              "'Sign Up'".format(request.form['username']))
        return redirect(url_for('index'))


# --------------------------------------------------------------------- Create new user
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
            name = user_details['first-name'].title()
            session['name'] = name
            return redirect(url_for('get_types'))
        else:
            flash("'{}' has already been taken. Please try another username".format(user_details['username']))
            return redirect(url_for('index'))

# --------------------------------------------------------------------- Logout
@app.route('/logout')
def logout():
    """ Function to log the user out by clearing the session """

    session.clear()
    return redirect(url_for('index'))

# --------------------------------------------------------------------- Landing page
@app.route('/get_types', endpoint='get_types')
@login_required
def get_types():
    """ Display training types """

    return render_template('get_types.html', title='Training Types')


# --------------------------------------------------------------------- Recipes
@app.route('/recipes/<field>/<type>', endpoint='recipes')
@login_required
def recipes(field, type):
    """ Render template displaying all recipes in a summarised view from 'recipes' collection """

    if field and type:
        if field == 'training_type':
            training_type = {'training_type': type}

            recipe = mongo.db.recipes.find(training_type)
            return render_template('recipes.html', recipes=recipe, title=type)
        elif field == 'meal_time':
            meal_time = {'meal_time': type}

            recipe = mongo.db.recipes.find(meal_time)
            return render_template('recipes.html', recipes=recipe, title=type)
        else:
            recipe = mongo.db.recipes.find()
            return render_template('recipes.html', title='Recipes', recipes=recipe)
    else:
        recipe = mongo.db.recipes.find()
        return render_template('recipes.html', title='Recipes', recipes=recipe)

# --------------------------------------------------------------------- Recipe detail
@app.route('/recipe_detail/<recipe_id>', endpoint='recipe_detail')
@login_required
def recipe_detail(recipe_id):
    """ Render template to display a recipe in detail """

    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('recipe_detail.html', recipe=recipe)

# --------------------------------------------------------------------- Add recipe form
@app.route('/add_recipe', endpoint='add_recipe')
@login_required
def add_recipe():
    """ Render template displaying form to add new recipe """

    return render_template('add_recipe.html', title='Add Recipe')


# --------------------------------------------------------------------- Insert recipe
@app.route('/insert_recipe', endpoint='insert_recipe', methods=["GET", "POST"])
@login_required
def insert_recipe():
    """ Logic to insert new recipe into 'recipes' collection from add_recipe"""

    recipe = mongo.db.recipes

    if request.method == "POST":
        upvote_default = 0
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
            "rating": request.form["rating"],
            "upvotes": upvote_default,
            "allergens": allergens,
            "ingredients": ingredients,
            "method": methods
        }
        recipe.insert_one(recipe_details)

        return redirect(url_for('recipes', field='recipes', type='all'))


# --------------------------------------------------------------------- Edit recipe
@app.route('/edit_recipe/<recipe_id>', endpoint='edit_recipe')
@login_required
def edit_recipe(recipe_id):
    """ Render the edit_recipe page for the recipe to be updated """

    difficulty = ['Easy', 'Medium', 'Hard']
    meal_time = ['Breakfast', 'Lunch', 'Dinner']
    training_types = ['endurance', 'power', 'speed', 'strength']
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=recipe, training_types=training_types, difficulty=difficulty,
                           meal_time=meal_time)

# --------------------------------------------------------------------- Update recipe
@app.route('/update_recipe/<recipe_id>', endpoint='update_recipe', methods=["GET", "POST"])
@login_required
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

    if request.form.get("rating") != recipe["rating"]:
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                    {"$set": {"rating": request.form.get("rating")}})

    if request.form.get("ingredients") is not None:
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                {"$set": {"ingredients": request.form.getlist("ingredients")}})

    if request.form.get("method") is not None:
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
                                {"$set": {"method": request.form.getlist("method")}})

    return redirect(url_for('recipe_detail', recipe_id=recipe_id))

# --------------------------------------------------------------------- Delete recipes
@app.route('/delete_recipe/<recipe_id>', endpoint='delete_recipe', methods=['GET', 'POST'])
@login_required
def delete_recipe(recipe_id):
    """ Delete recipe """

    # Get the recipe to delete
    recipe_to_delete = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # Delete the recipe from the db
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})

    # Let the user know the recipe has been deleted
    flash("'{}' was successfully deleted.".format(recipe_to_delete['name_of_recipe'].title()))

    return redirect(url_for('recipes', field='recipes', type='all'))

# --------------------------------------------------------------------- Upvotes
@app.route('/upvote/<recipe_id>', endpoint='upvote', methods=['GET', 'POST'])
@login_required
def upvote(recipe_id):
    """ Increment upvote for the recipe """

    mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)},
                                {"$inc": {"upvotes": 1}})
    return redirect(url_for('recipe_detail', recipe_id=recipe_id))

# --------------------------------------------------------------------- High/Low
@app.route('/sort_by/<field>/<high_low>', endpoint='sort_by')
@login_required
def sort_by(field, high_low):
    """ Display recipes with the highest ratings to the lowest """

    if field:
        if high_low == 'high':
            value = -1
        elif high_low == 'low':
            value = 1
        recipe = mongo.db.recipes.find({'$query': {}, '$orderby': {field: value}})
        return render_template('recipes.html', recipes=recipe, title='Recipes')
    else:
        flash('Ooops, looks that we could not process your request.')
        return redirect(url_for('recipes', field='recipes', type='all'))


# --------------------------------------------------------------------- statistics
@app.route('/statistics', endpoint='statistics')
@login_required
def statistics():
    """ Page display data visualization about statistics for the recipes """

    # Count how many recipes have each meal time to send to the pie chart
    breakfast = mongo.db.recipes.find({'meal_time': 'breakfast'}).count()
    lunch = mongo.db.recipes.find({'meal_time': 'lunch'}).count()
    dinner = mongo.db.recipes.find({'meal_time': 'dinner'}).count()

    # Build pie chart
    pie_chart = Pie()
    pie_chart.title = 'Meal Times'
    pie_chart.add('Breakfast', breakfast)
    pie_chart.add('Lunch', lunch)
    pie_chart.add('Dinner', dinner)
    pie_chart = pie_chart.render_data_uri()

    # Count how many recipes have each training type to send to line chart
    endurance = mongo.db.recipes.find({'training_type': 'endurance'}).count()
    speed = mongo.db.recipes.find({'training_type': 'speed'}).count()
    strength = mongo.db.recipes.find({'training_type': 'strength'}).count()
    power = mongo.db.recipes.find({'training_type': 'power'}).count()

    # Build line chart
    line_chart = Bar()
    line_chart.title = 'Training Types'
    line_chart.add('Endurance', [{'value': endurance, 'label': 'Endurance'}])
    line_chart.add('Strength', [{'value': strength, 'label': 'Strength'}])
    line_chart.add('Power', [{'value': power, 'label': 'Power'}])
    line_chart.add('Speed', [{'value': speed, 'label': 'Speed'}])
    line_chart = line_chart.render_data_uri()

    return render_template('statists.html', title='Statistics', pie_chart=pie_chart, line_chart=line_chart)


if __name__ == '__main__':
    port = int( os.getenv("PORT") )
    host = os.getenv("IP")
    app.run(host=host, port=port)