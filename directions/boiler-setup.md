# Welcome to the Flower Shop

You have been tasked to build an app that will allow the employees of the flower shop to manage the different bouquets that the shop builds for it's customers.

## Project Setup
* Clone down the repo and `cd` into it
    * `git clone --single-branch --branch tct-setup https://github.com/TrinityTerry/py-dj-flowershop.git`

* Change this from a git repo to a regular directory:
  * `rm -rf .git`

* Create a new repository on Github and make your first commit:
  * Create a brand new repository under your account on Github
  * `git init`
  * `git add .`
  * `git commit -m "First commit"`
  * `git remote add origin your-new-repos-ssh-remote-url`
  * `git push -u origin master`

* Create your OSX/Linux OS virtual environment in Terminal:
  * `python -m venv flowershopenv`
  * `source ./flowershopenv/bin/activate`

* Install the app's dependencies:
  * `pip install -r requirements.txt`

* All your models and migrations have already been created, so ahead and run migrations:
  * `python manage.py migrate`

* Create a superuser for your local version of the app:
  * `python manage.py createsuperuser`

* Populate your database with initial data from fixtures files: (_NOTE: every time you run this it will remove existing data and repopulate the tables_)
  * `python manage.py loaddata flowers`
  * `python manage.py loaddata bouquets`
  * `python manage.py loaddata bouquet_flowers`

* Make a copy of `bouquetapp/views/connection.py.example` and remove the `.example` extension and change the path to the database 

* Fire up your dev server and get to work!
  * `python manage.py runserver`