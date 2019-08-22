##Aim

Being a vegetarian and a fitness fanatic in the western world I have often found it hard to find one place with good 
vegetarian recipes categorized by training type. 

After a hard strength building session I would love to be able to find a tasty recipe that will fulfill my protein 
needs. Before I hit the track to try and beat my 100m PB, it would be great to get the right food into me that will 
help break records. The same would be amazing when training to increase endurance or power.

So with all the above in mind I designed and built a handy web application to achieve this - 
[Meat Free](https://meat-free.herokuapp.com).

Meat Free is an online cookbook that allows site users to share, edit and read cooking recipes for vegetarian athletes.

##UX

Starting with a mobile first design approach to this project I started creating mockups and wireframes for mobile 
and small screens. I then moved onto creating mockups and wireframes for medium and larger screens. The design of the 
site is cool, cheeky and fun.

Mockups and wireframes can be viewed via this link - Mockups/wireframes.

Below are user stories that were conducted in order to gain clear goals that needed to be achieved for this website.

 
1. I want a cookbook for vegetarian athletes.
2. I want recipes organized by endurance, speed, power and strength.  
3. I want to see all recipes in a summarised view.
4. I want the ability to display the summarised view based on category or attribute.
5. I want the ability to display the summarised view in different orders based on ratings, upvotes, difficulty etc. 
6. I want a page that displays statistics in a visually appealing way.
7. Have a detailed view for each recipe that shows all attributes and full preparation instructions.
8. To have the ability to create, update and delete recipes.
9. I want to be able to upvote on recipes I like.
10. I want to be able to provide a rating to the recipe I add.


The navigation bar is responsive having break points for smaller, medium and large screens. The navigation links 
disappear on screen width below 992 pixels and a burger menu icon appears top left. When the burger icon is clicked, 
it brings a side navigation bar across from the left. The navigation bar is fixed to the top and follows the use down 
the page for ease of navigation.

When a user first visits the site they are presented with a clean simple login form with links to a sign up form if 
they do not have an account. Leaving out a navigation bar and rendering the logo center just above the forms gives an 
elegant look and great first-impression.

The landing-page once signed in welcomes the user with a lovely image of fresh vegetables. Scrolling down the user is 
presented with some small content to explain the website and how to use it. The cards underneath when clicked on will 
take the user straight to a summarized view displaying all recipes under that training type.

Recipes is the main summarized view with a number all filters that can be used. Each summarized card displays a small 
amount facts and description about the recipe with links to view the recipe in its full glory.

The Recipe Details view displays the recipe is a clean simple manner. Care was taken to not clutter this view as most 
online cookbooks seem to have so much going on in the page that just reading the list of ingredients can be a task in 
itself. I believe I have achieved this with its simple layout and use of soft colours and images.

The Edit and Add Recipes forms use a mix of input fields to help break up the forms and let the user interactive in 
more than one way. The plus and minus symbols let the user add or remove input fields for ingredients and methods. 
By doing this the forms can be kept more compact to help with adding or editing on smaller devices.

To show some stats the Statistics page produces some nice graphs to help visualize what is in the database. The graphs 
are interactivate giving the website some more functionality.

##Features

The list below shows all the added features that needed to be in place for the project to be fully functional. The 
features planned to be added in the future are listed in the “Future Features” section of this document.

####Freatures on this website are:

* Login - allows user to login
* Sign Up - Sign up new users
* Training Type cards - allows users to navigate straight to recipes for that training type
* Recipes - shows summarized view of all recipes 
* Recipes filters - allows different filters to be applied to a summarized view
* Recipes details - Detail display of a recipe
* Add recipes, update recipes and delete recipes
* Statistics - data visualisation

####Future features

* Full user account functionality with password protection
* Ability for users to follow other users 
* Notification system to alert users of new recipes added by users they follow
* Pagination 

##Database Schema

I chose to use a document store type database using Mongodb for the database for this application. My reason for this 
is each document can hold all the attributes and data for each recipe with no relationships needed to be created to 
other recipes or data. 

There are two collections, one called ‘recipes’ which houses all the recipe details, and once call ‘user_accounts’ to 
house user account details. 

##Technologies Used

Below are a list of the programming languages, technologies and frameworks used for this website.

* HTML5
* CSS3
* JavaScript
* JQuery
    * Materialize plugins.
* Markdown
    * Used to write README.md file.
* [MongoDB](https://cloud.mongodb.com)
    * Document-oriented database used for the application database.
* [Materialize](https://materializecss.com) 0.100.2 framework
    * The website uses Materialize CSS framework for its styling, grid system, page layout, button styling, icons and 
    response navigation bar.
* [PyCharm CE IDE](https://www.jetbrains.com/pycharm/)
    * PyCharm Community Edition was used as the IDE to write the web application.
* [Marvel App](https://marvelapp)
    * This was used to design and create the wireframe for this project.
* [Google Fonts](https://fonts.google.com)
* Git
    * Version control
* [Github](https://github.com)
    * Remote repository
* Google Chrome Developer Tools
* Firefox Inspector
* Google Docs
    * Write the contents of the README.md file.

##Testing

I conducted testing across different platforms and web browsers in order to make sure the website worked correctly and 
looked great across each one. I also asked friends and family to test across their own devices and to give me honest 
opinions and feedback.

Platforms:

* Samsung Galaxy 8
    * Google Chrome
    * FireFox
    * Samsung web browser
* iPad Mini
    * Safari
* Macbook Pro
    * Google Chrome
    * FireFox
    * Safari
* Ubuntu 18.0
    * Google Chrome
    * FireFox
* Windows 10
    * Google Chrome
    * FireFox
    * Mircosoft Edge
    * IE 11
    
Manual testing was conducted to ensure the user story objectives were achieved.

1. I want recipes organized by endurance, speed, power and strength.
    * Login
    * Click on each training type on the landing page. Summarised view with training type as page title and heading 
    with recipes of that training type listed below.
2. I want to see all recipes in a summarised view.
    * Click on ‘Recipes’ in the navigation bar. Summarised view displaying all recipes.
3. I want the ability to display the summarised view based on category or attribute.
    * Click on ‘Recipes’ in the navigation bar.
    * Click on each option in the dropdown menu for ‘Training Type’ and also ‘Meal Times’. Summarized view displayed 
    recipes based on the option selected.
    * Click on each training type card on the landing page.
    * Repeat step 3b for each training type.
4. I want the ability to display the summarised view in different orders based on ratings, upvotes, difficulty etc. 
    * Click on ‘Recipes’ in the navigation bar.
    * Using the ‘Sort By’ drop down menu select each option. The summarised view changes the order of the recipes based 
    on the filter applied.
5. I want a page that displays statistics in a visually appealing way.
    * Click on ‘Statistics’ in the navigation bar. Graphs show statistics about the recipes in the database are 
    displayed.
6.  Have a detailed view for each recipe that shows all attributes and full preparation instructions.
    * Click on ‘Recipes’ in the navigation bar.
    * Click on ‘Click for full recipe’ on a recipe card. Recipes details page renders displaying the recipe in details.
7. To have the ability to create, update and delete recipes.
    * Create Recipes
         * Click on ‘Add Recipes’ in the navigation bar.
         * Complete the Add Recipes form.
         * Click ‘Add Recipe’ button and the recipe with be inserted into the database.
         * Click ‘Recipes’, the recipe added is being displayed in a summarized card. 
         * Click on ‘Click for full recipe details’ on the recipe card. The recipe with be displayed in detail.
    * Update Recipes
        * Click on ‘Recipes in the navigation bar.
        * Click on ‘Click for full recipes’ on a recipe card.
        * Scroll to the bottom and click ‘Edit Recipe’ to see the recipe loaded into a form which can be edited.
        * Edit the recipe and click ‘Update Recipe’.
        * Viewing the recipe details the recipes has been updated with the change made on the form.
    * Delete Recipes
        * Click on ‘Recipes’ in the navigation bar.
        * Click on ‘Click for full recipes’ on a recipe card.
        * Scroll to the bottom and click ‘Edit Recipe’ to see the recipe loaded into a form which can be edited.
        * Click on ‘Delete’ and confirm deletion in the modal.
        * The recipe is no longer in the database and no longer appears on the website.
8. I want to be able to upvote on recipes I like.
    * Click on a ‘Click for full recipe’ on a recipe card.
    * Click on the thumbs up icon to give the recipe an upvotes and the number under the icon will increment by one.
9. I want to be able to provide a rating to the recipe I added.
    * Click on ‘Add Recipes’ in the navigation bar.
    * Enter a number in the ‘Rate this recipe’ field.
    * Complete the rest of the form.
    * Click the ‘Add Recipe’ button and see the rating given to that recipe on its recipe card in a summarised view 
    and in its detail view.
    
Further testing was conducted for adding recipes and editing recipes to ensure no errors would occur. 

While conducting this testing I found that select elements could not contain disabled selected attributes in the 
edit_recipes form. This was causing a bad request to the database if the dropdown menus had not been altered. 
I solved this issue by first passing the value in the database and then using an if else block I passed in variables 
from a list that were not in the database to create the list options. 

##Depolyment

The web application was created using PyCharm CE IDE. Git was used for version control and pushed to a remote 
repository hosted on Github.

The web application is deployed using Heroku and can viewed here - Meat Free

The web application was built and tested locally and once near completion it was pushed to Heroku by linking the 
master git branch from the remote Github repository to the app created in Heroku. All changes pushed to the master 
Github branch automatically pushed to the production application in Heroku. 

To ensure additional features and testing was conducted before being pushed to the production environment in Heroku. 
I created a development branch in git. All changes were pushed with commits first to the development branch then once 
happy merged into the master branch. Then as mentioned this would automatically push to the production environment.

Deploying the application at a later stage I encounter issues with Heroku not detecting the correct build-pack. After 
troubleshooting and looking up the Heroku error I found that I needed to supply a runtime.txt file to tell Heroku what 
version of Python the application was using. I also had to install and set Gunicorn in the Procfile for the application 
to build successfully.

There are no differences between the deployed version of the project found here and its development version.

####How to deploy the code locally

If you wish to run this code locally then please follow the instructions below.

1. Download the code from the Github repository at https://github.com/AnthonyNicklin/meat-free.
2. Click on Clone or download then Download ZIP. This will download the code into a ZIP folder locally on your computer.
3. Uncompress the ZIP folder.
4. Create a virtual environment. Tutorial of how to create a virtual environment can be found here 
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/.
5. Activate the virtual environment.
6. Install the necessary Python packages in the requirements.txt file.
    * ````pip3 install -r requirements.txt````
7. Create a secret key and set as environment variable.
    * MacOS and Linux ````export SECRET_KEY=<secret key>````
    * Windows ````set SECRET_KEY=<secret key>````
8. Tell Flask how to import the app.
    * MacOS and Linux ````export FLASK_APP=meat_free.py````
    * Windows ````set FLASK_APP=meat_free.py````
9. Connect your MongoDB database to the application. If you have not created a MongoDB database please follow the 
instructions under the heading ‘Create a MongoDB account’.
    * Set MongoDB URI as environment variable.
        * MacOS and Linux ````export MONGO_URI=<mongo_uri>````
        * Windows ````set MONGO_URI=<mongo_uri>````
    * Create a database and two collections. One called ‘recipes’ and the second ‘user_accounts’.
    * Set MongoDB database name as environment variable.
        * MacOS and Linux ````export MONGO_DBNAME=<mongo_DBNAME>````
        * Windows ````set MONGO_DBNAME=<mongo_DBNAME>````
10. Open up a terminal and run ````flask run````.
11. Navigate to the address the terminal returns to view Meat Free.

####Deploy to Heroku

This project was deployed to Heroku and uses Heroku for its production environment. Instructions are below on how to 
deploy this web application to a production environment in Heroku.


*Git must be installed onto your computer. Instructions for installing Git can be found here 
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git.

**Heroku CLI must be installed in order to deploy to Heroku using these instructions. Please follow the instructions 
here to download and install Heroku CLI https://devcenter.heroku.com/articles/heroku-cli.

***You must have a MongoDB account and database setup with two collections created called ‘recipes’ and ‘user_accounts’. 
Follow the instructions under the heading ‘Creating a MongoDB account’.

1. Open up Heroku and navigate to your dashboard.
2. Select New > Create New App and fill out the details required then hit Create App.
3. Select Settings > Reveal Config Vars
    * Enter in the following environment variables:
        * SECRET_KEY:	secret key
        * MONGO_URI:	    mongo uri
        * MONGO_DBNAME:	mongo dbname
        * FLASK_APP:		meat_free.py
        * IP:			0.0.0.0
        * PORT:			80
4. Download the code from the Github repository at https://github.com/AnthonyNicklin/meat-free.
5. Click on Clone or download then Download ZIP. This will download the code into a ZIP folder locally on your computer.
6. Uncompress the ZIP folder.
7. Open up a terminal or cmd prompt and login into Heroku CLI.
    * ````heroku login````
8. Check the app is present.
    * ````heroku apps````
9. A runtime.txt and Proflice have already been created for this project but make sure they are present. If for some 
reason they are not then follow the steps below to create them.
    * Runtime.txt
        * Create a new text file in the root directory of the project and add ‘python-3.6.6’ to the file.
    * Procfile
        * In a terminal make sure you are in the root directory of the project then run ````touch Profile````.
        * Add the following text to the Procfile ‘web: flask translate compile; gunicorn meat_free:app’.
10. Add a new git remote for Heroku.
    * ````git remote add heroku git@heroku.comYOUR_APP_NAME.git````
11. Push to Heroku.
    * ````git push heroku master````
12. Give Heroku a few minutes to get it all set up and then check the activity logs under Activity tab in your Heroku 
dashboard. 
13. Once the build is complete click on Open App top right to see Meat Free in action.

###MongoDB
####Create a MongoDB Account

The database used for this application is MongoDB and a free account can be created at https://www.mongodb.com/new.

1. Click on Try Free top right
2. In the right hand panel complete the fields and complete verification steps required
3. Click on Build a New Cluster.
    * Select your preferred Cloud provider (I go with AWS).
    * Select the region you wish to host and be sure to check the region is in the free tier.  
    * Select a Cluster Tier. Again be careful to select a free one if you wish to host this for free.
    * Select any additional settings you wish to set.
    * Give the Cluster a name.
    * Check settings then once happy select Create Cluster.
4. Click on Collections > Create Database.
    * Give it a name (remember this as you will need the database name for import settings when deploying the code).
5. Click on Create Collection.  
    * Create one with a name of ‘recipes’ and another with a name of ‘user_accounts’.
6. Click on the Overview tab then Connect.
    * Click on Connect Your Application
    * Select the correct drive and version.
    * Copy and past the Connection String and keep this safe as you will need it for your MONGO_URI variable to deploy 
    the code.
    
##Credits
####Content

Recipes where taken from a number of websites with the authors of the recipes being credited in the web application 
under each recipe.

####Images

All images for this web application are being used under free commercial license from Pixaby. Links to each image are 
below.


* [Avocado](https://pixabay.com/illustrations/avocado-green-food-healthy-3651037/)
* [Beetroot](https://pixabay.com/vectors/beet-beetroot-vegetable-root-plant-25383/)
* [Carrot](https://pixabay.com/vectors/carrot-root-vegetable-orange-33625/)
* [Garlic](https://pixabay.com/vectors/garlic-cloves-vegetable-organic-25382/)
* [Landing Image](https://pixabay.com/photos/casserole-dish-vegetable-tomato-2776735/)


####Logo

The carrot icon was taken from Pixaby under free commercial license. The writing Meat Free was created using Google 
Fonts Mountains of Christmas. Using Adobe Xd I added the font and image together and created different backgrounds 
for the image to be used on different pages.











 