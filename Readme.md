nc-airbnb-model-backend

Download python newest version make sure it is < 3.0 as of 09/02/2022.
Install poetry - Poetry is going to allow us to create a virtual environment. 

*What is poetry?*

- Django is a package that we need to download. 
- Poetry allows us to download and manage packages.

*What is virtual environment?*
- Virtual environment like a bubble.
- Virtual environments allow you to download same package with different versions. so that different versions could be used on seperate projects.
- Example: Use Django virtual environment latest version. 

*How do you create a virtual environment?*
- poetry init. 
-- Interactive guide to create a package. 
-- Just enter on everything. 
-- say yes. 
Output: 
- pyproject.toml gets created: contains description of the virtual environment and the version of python and settings. 

*How do you get inside the bubble?*
1. Enter into a poetry shell. 
```
poetry shell
```
2. Test your VE by running Django Admin command
```
django-admin
```
3. Run 'Exit' to exit the VE.

*How do you start Django project within the folder that you already created?*
```
django-admin startproject config .
```

*Pacakge to install .gitignore*
Download Gitignore and run the command pallete to create gitignore. 

*How do you know which methods are available in a class?*
- If you print with dir(), you can view all the classes available for use. 
```
print(dir(jia))
```
- Then, you can google what methods do. 

*How do you run the server?*
- You can use the manage.py to run the server. 
```Py
python manage.py runserver
# Output: Django app runs.
```

- There are two issues:
1. Red letters
2. /admin doesn't route. 

Reason:
Django is looking for a DB called Django session but you don't see it. 
db.sqlite3 is the default DB automatically created when you start a project. 
How do we create a django session table. 

*What is migration?*
- you want to modify the shape of the DB. 
- you are commanding django to create django session table. 
Error: You have 18 unapplied migration(s).

*How do you apply the migration?*
use python manage.py migrate
- Python ran files in 18 files. 
- If you open the Db, you will see text. 

Now, the admin panel is working. 

Recap:
- Django wants to use DB to data of the users and session. 
- Django is using for auth_user. This is emtpy. 
- Django wants to shape the DB according to the form. 

# Super User

- Admin page is provided. 
- Go to Django admin page. 
- you have to enter the virtual environment again. 

*How do you create a superuser?*
```
python manage.py createsuperuser
```
- If you put an easy password, django will notify you to complicate.

Admin panel
- User: edit, delete, filter.
- Grouops
- Searh user
- Hashed pwd
- User data

*What are the difference between the framework and library?*
- Library is something that developers call.
- Framework is something that calls our code.
- If you change the variable or add the variables into setting.py, it will change the django setting because django is calling the variables from the setting.py. 

*What other framework features that we need to know?*
- setting.py: 
- url.py: look for url routes.

# Apps

- Concept of apps 
- Imagine folders with logic, they are applications. 
- Folder that is for rooms. 
- We are performing many operations within the photo.
- Ex:
Room logics:
Add room
Add photos.
User:
Authentication
- DJango app encapsulate data and logic.
- Apps might link but they shouldn't be in the same folder. 

# Django App

*How do you create a first application?*

- Create houses app
```bash
python manage.py startapp houses

```

*Overview of the file structure*
- migrations
- __init__.py
- admin.py: register model.
- apps.py
- models.py: describe the shape of your data.

*How do I create a first model?*

- In models.py, below is the example.
```py

""" Model Definition for Houses"""
class House(modesl.Model):
    # There are many data fields that you can choose from
    name= models.CharField(max_length=140)
    # Price can't be negative; Django will give warning if price becomes negative.
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)

```

- When you save the file, django doesn' know this change because django is not aware of the house application yet. 
- In order for it to recognize, you ahve to put it in the INSTALLED_APPS variable in the setting.py.
settings.py
```py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "houses.apps.HousesConfig",
]
```

- The moment you put it in the installed_apps, Django will start checking the models.py in the house app. 

# App Migrattion

- Django needs to talk to DB. 
- DJango talks to DB by translating to SQL code. 
- Automatically generate admin panel for your custom data. 

*How do you genearate admin panel for your custom data?*

Steps:
1. Register your model.
2. Create a class that inherit from the admin panel. 
3. Django will connect your model to the admin panel.

```py
from django.contrib import admin
from .models import House

# Register your models called House in the admin panel.
@admin.register(House)

# Class inherit everything from the ModelAdmin.
# Create a class called HouseAdmin
# HouseAdmin inherits everything from admin panel for your model.
# ModelAdmin is in admin panel.
class HouseAdmin(admin.ModelAdmin):
    pass

```
Error when you click the house app in the admin panel.
- The error happens because Django is looking for a table and the django is looking for a table in the DB. 

- We have to inform our DB about our house model. 
- migration modifies the shape of DB so we migrate. 

*How do you perform app migration?*
```
python manage.py makemigrations
```

Django created a model called house. under the path below:
houses\migrations\0001_initial.py
