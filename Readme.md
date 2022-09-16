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

*How do you add Django App?*

- Please make sure that you are inside of the project folder, and run below command.
```
poetry add django
```
**Output: poetry.lock got created.**

*How do you get inside the bubble?*
- Enter into a poetry shell. 
```
poetry shell
```
- Test your VE by running Django Admin command
```
django-admin
```
-  Run 'Exit' to exit the VE.

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

*We can now migrate to DB*
```
python manage.py migrate
```

in the admin panel, you can add fields in the DB through admin panel. (input fields are created in the admin panel. )

Recap:
Put your mouse on top and you will see all the fields that you can put.

# Admin

- Django is a framework. 
- When you print a class, you will get a "House Object". 
- If you mention the string method, it will brint

*How do you create more columns in the admin panel?*
Add list_display = [] to the class

```py
class HouseAdmin(admin.ModelAdmin):
    # 
    liste_display = [
        "name", 
        "price_per_night",
        "address",
        "pets_allowed"
    ]
    # Create a filter
    list_filter = [
    "price_per_night",
    "pets_allowed"
    ]
    # Search for address
    search_fields = ["address_startswith"] # search an house that starts with.
    

```

*More actions?*
```py


```

# Documentation

Field examples:

- Field.default: Set a default field.
- Field.editable: the field will not be displayed in the admin or any other ModelForm if it is not editable or False.
- Field.help_text: Extra "help" text for the widget. The texts are displayed on the below of the text.
- Field.type:
- AutoField:
- BigIntegerField: For big integers.
- max_length:
- DurationField
- FileField:
- FilePath
- Float
- ImageField:

**If you want to customize your admin, you have to create a class and register model.**

- ModelAdmin: actions are the things that you see ont he 
- fieldsets - allow you to show or hide things in the admin panel. 
- filter_vertical 
- list_display: shows the columns.

# User App

- Some app functionality and permission management are out-of the box. As you grow your apps and create model, more will come in the permission section. 


- You want to customize it littlebit more. 
Addiing what:
- Profile, profile photo, github, kakao more authentication.

*What are ways to customize users?*

1. Most people:
a. Django user system
b. Create a Profile model.
c. Connect them to authenticate.
d. Profile will have other authentication options.

**In the documentation, it is highly recommended to create a custom model.**

- Changing to user model mid-project. 
- The first thing is to create cutom model with your own. 

- Install pylance: python server for a VScode.
```py
# Scriggly lines.
from django.db import models
```
- You have to select the virtual environment to let pylance recognize the python in the bubble. 
- If not, you have to select the python in the bubble by doing cmd + shift + p. 
```
cmd(ctrl) + shift + p
> python select interpreter
```

# Custom model

- Create a user application. 
Steps:
a. Create a Django app
```py
python manage.py startapp users
``` 
- Follow the documentation
b. Create a custome user by inheriting everything that Django has. 

c. Under users/models.py, you inherit everything from the Django side. 
- you can reuse the users that Django uses.
```py
from django.db import models
from django.contrib.auth.models import AbstractUsers. 
# If you hold a control key and go into the AbstractUsers class, you can see bunch of user attributes that you can inherit.
```

- Within the part of the Abstract User, we are replacing "Class User(AbstractUser)"

d. Tell Django that you want to use your own user. 

- Setting.py: go to #auth and copy paste the name of the setting.
settings.py
```py
# Auth

AUTH_USER_MODEL = "users.User"
```
- Add the new app to the CUSTOM_APP var of the settings.py.

- Since the Django is using the User_model that it already has, we have to delete some files.
(You have to replace from the beginning.)
Files that you are deleting:
db.sqlite3
migration files from your houses
migrations/
0001, 0002

- Before you start you server again, you have to run migrations. 
```
python manage.py makemigration users
python manage.py migrate
```

- Create superusers
- Run server
- When you look into the Admin panel, you see that users are organized under a seperate section. This is good because we can customize the users. 

## Custom Fields

- If you press CTRL and AbstractUser, you will see the source codes. 
- If you like the users to only have names, you can do that in the users/model.py
**Never Modify the source code of the django.**
Examples of custom User:
```py
# from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150)
    is_host = models.BooleanField()
```
- It is very important that you makemigration becauase you can sync the shape of your model in the python code to DB shape. 
```
python manage.py makemigrations
```

Error: 
```
This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py
```
- DB needs to have something to populate on the existing rows. 

- We are going to understand why is it happen!

## Defaults

*Why do you get OperationalERror?"*
Error: 
OperationalError at /admin/users/user/
No such column: users_user.name
- Our DB
    - users, and houses tables. 
    - if you add new column or new atttributes, you need to have default value because Django doesn't know what goes into the new attributes of existing users. 
    - This happen because there are non-nullable values such as Boolean.
    - If it was nullable values, django will put NULL. 

Solution:
- Make the value nullable or set the default value.


*However, it shows an error again!*

*Why do you get FieldError?*
'first_name' cannot be specified for User model form as it is a non-editable fields. 
- This happens because admin by default can have edittable first and last name. 

## Custom Admin

- We are going to look at the fieldsets. 
- You can put fields into sections. 

admin.py
```py
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("Profile", 
            {"fields": 
                ("username", "password", "name", 
                )
            }
        )
    )
```

- You can add classes ("collapse") to make it collapsable. 


# Foreign Keys

*How to connect models to each other?*

- Since many apps and models have connection with each other, we have to learn how to connect models to each other. 

- Foreign keys are just like IDs. 
- In the Django documentation, it is called pk. 
- Houses and Users have IDs. 
- Type of the column would be the *foreign key*
- Django will know that numbers that you provided are the ID in the User DB. 
- Django will search for the user and utilize that data.
```python
    owner = models.ForeignKey(
        "users.User", 
        on_delete=models.CASCADE
        )
```

## Super Recap
- IF the user with the ID gets deleted the house gets deleted as well if their information is related with CASCADE. 

# 6 Models and Admin

- Create a profile photo. 
- Import ImageField - need to install Pillow. 
- In stall pillow from your poetry. 
```
poetry add Pillow 
```
- Need to migrate later...
- Create GenerChoices 

user/models.py
```py


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    profile_photo = models.ImageField()
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
    )

```

- Once you added new models, you migrate.
- After you add model, you add the values inside the admin.py.
- You will see that there are additioal models populated on the user in the admin panel. 
- blank=true allows the field not required to be empty. 
- All these information gets saved on the postgresql. 

# Room Model 

- Create room application
- Add it to the CUSTOM_APPS in the setting. 

- Room inherit from the models.Model
- Add Country and other variables. 


models.py
```py
class Room(models.Model):
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length)
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models
```


```
class RoomKindChoices(models.TextChoices):
    
```

- Create a model called "Amenity"
- The room page shows what they offer.
- This will unlock a new concept called many-to-many.
```py
class Amenity(models.Model):
    """ Amenity Definition """
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, default="")
```
- Again, ondelete will delete when the user is deleted. 
- 

# Many to Many relationship

*What is the meaning of many to one and one to many*

Many to One
ex: Many rooms and belong to the same user. 

One to Many
ex: one user can have many rooms. 
```py
owner = models.ForeignKey(
    "users.User",
    on_delete=models.CASCADE,

)
```

Many to Many
- Many to Many relationship means that 
[Amenity1, Amenity2, and Amenity3] can be used by all Rooms [Room1, Room2, Room3]

- Admin Panel will help us visualize these concepts.
- We have to go to rooms and add below

```py
amenities = models.ManyToManyField("rooms.Amenity")
```

auto_now_add = set the field to right now when the object is first created. 

- Create one more application that you are going to be shared by one application. 
- Common model could be the models that other users use as a blueprint
```py
class CommonModel(models.Model):
    """Common Model Definition"""
    created_at = models.DateTimeField(auto_new_add=True)
    updated_at = models.DateTimeField(auto_new=True)

    class Meta:
        abstract = True

```
- RECAP: a new app called common will be shared across the multiple apps. 

Many to Many: Many rooms can have many amenities.
Foriegn key: one user upload one room.

Django should be ignore Common model because we don't want to create a table for created_at everytime they look at the object. 

blank_true vs null_true

# Rooms Admin

*How do you show a class as a string?*
- __str__ method will acomplish this. 

```py
def __str__(self) ->str:
    return self.name
```

- If you want to create a filter in the admin, you can create a filter by using a list_filter var.
-"auto_now=True" automatically create var.

# 6.5 Experience

- Experiences model 
- Create app
- Update setting.py
- Foreign: when the user is deleted, you delete all other var associated. (on_delete)
- Create all the fields with corresponding fieldtypes. 

# 6.7

- Users can create a review
- App > setting

```py
class Review(CommonModel):
    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        "rooms.Rooms"
        null=True,
        blank=True
        on_delete=models.SET_NULL,
        )

```

- Django calls str method of the review on the admin panel 

# Wishlists

- Wishlists is when the user comes and they like a room or an experience. 
- You can create a wishlist or add a room to a wishlist. 
- Add a wishlist app
- put it in custom_app of setting.py
- 
*Create ManytoMany relationship:*
```py
rooms = models.ManyToManyField(
    "rooms.Room",
)

```
- After you migrate, you will see them in the admin panel. YOu can create an object yourself.
- You can add def __str__ method if you want your object to look nicer. 


# Bookings

- Users can book or they can book from rooms. They can check in with the date, you can reserve. 
- This model can be created within an app called Bookings or reservation. 
- ONe users can have many bookings but booking can only have one user.
- One-To-Many: Foriegn key. 

Room: Can one booking has many rooms? no. Booking can have one room. One room can have many bookings. 
- One-To-Many: This is a foreign key.
- even if experience gets deleted, users should still know what they booked. 
on_delete= models.SET_NULL,

- Booking Model:
    - User - ForeignKey() - one to many.
        - on_delete = models.CASCADE.
        - If user deleted, booking gets deleted.
    - Room - ForeignKey() - one to many
        - on_delete=models.SET_NULL.
        - null=True
        - blan=True: for django admin form. 

    - Experience = models.ForiegnKey()
    - Check_in = models.DateField()
    - Check_out = models.DateField()

- makemigrations -> migrate

- Register to admin
@admin.register(Booking)
class Booking(admin.ModelAdmin):
    list_display = {
        "kind",
        "user",
        "room",
        "experience",
        "check_in",
        "check_out"

    }

# Medias 

- One room can have many photos and videos. 
Steps:
1. Startapp medias
2. Add medias app in the setting
3. Create two models (one for photos, one for videos)
4. 