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
4. Add model variables
- file = models.ImageField()
- description = models.CharField(max_length=140)
- room = models.ForeignKey(
    "rooms.Room",
    on_delete=models.CASCADE
)
5. Video class
    - If you use the foreign key, you can create many photos and they belong to the same room. 
    - experience = models.OneToOneField.
    - people use one to one when you have a user and a payment information. There shouldn't be the multiple payment information for one user. 
6. Register models and two classes. 

# Direct Messages

- Users in the Air BnB can send direct message to each other. 
- Create a direct_message or DMs
- Install an app in settings.py
- Go to models, create two models, in the room there are many users. 
- 
```py
from django.db imports models
from common.models import CommonModel

class Room(CommonModel):
    """ Room Model Definition"""
    # Many to Many because users can interact with other users.
    users = models.ManyToManyField(
        "users.User",
    )
    
class Message(commonModel):
    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        # message shouldn't get deleted even if the user gets deleted. 
        on_delete = models.SET_NULL
    )
    room = models.ForeignKey(
        "direct_messages.Room",
        # Message will be deleted if the room is deleted.
        on_delete=models.CASCADE.
    )

```

- Chatroom is pointing to the user. 

*How do you create a verbose_name*
direct_message/apps.py
```py
class DirectMessagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "direct_messages"
    verboses_name = "Direct Messages"
```

# ORM

*What is ORM?*
- Once you've created your data models, Django automatically gives you a database-abstraction API that lets you create, retrieve, update, and delete. 

- Since we created models, we need to how to access those data NOT from admin panel. 

*How do you access the database?*

1. you can use the 'python manage.py shell'.

- Model communicate with DB with the shape of your data. 
- Room.objects: access the object properties.

```py
from rooms.models import Room
# Get all the properties inside the model called Room.
Rooms.objects.all()
# returns a queryset.
<QuetySet [<Room: Beautifyl House in >]>

# Search by property name
Rooms.objects.get(name="Beautiful House in seoul.")
```
room.id
room.name
etc......
room.owner.
.save(): saves all the changes you made in shell. 

# Filter, get, create, delete

- QuerySet can be looped. 
- .get() is used when you want to search for something unique. - find with the primary key of 1 .get(pk=1)
- .filter() allows you to search
ex: 
```py
Room.objects.filter(pet_friendly=True)
# Output:

```
- .filter() has many capabilities. 
- Search for the room that has the word seoul.
```py
# Greater than 15
Rooms.objects.filter(price__gt=15)
```
- Other filter options:
- __contain
- __startswith
- These are called lookups.

Steps:
1. You have to import the model
2. Amenity.objects.create() - creates an object.

*How do you delete a data?*
Steps:
1. Get the object and put it in the variable. 
to_delete = Amenity.objects.get(pk=7)
2. Delete the object using .delete()
to_delete.delete()


# QuerySet

*What is QuerySet?*
- allows you to chain operation together. 
- If you want to chain filter (filter twice), queryset allows us to keep filtering. 
- room.objects.filter(pet_friendly=True).exclude(price__lt=15): price less than 15.

- lazy: it will give the data when you are asked specifically. 
```py
for room in Room.Objects.all():
    print(room.name)
```
Room.objects.filter(pet_friendly=True).count()

- QuerySet
    - lazy - doesn't kill db
    - It can chain filter. 

lookups and offsets

# Admin methods

- Lookups

*What is lookup?*
- iexact: insensitive exact
- If you not have to care about uppercase or lowercase, you would use icontains(insensitive)
- Rooms.objects.filter(created_at__year=2022)
- You can search by months and peform gt operation.
- QuerySet API reference.


Admin methods
- We can create a better panel for our admin. 
- We can put our own functions in the admin panel. 
- You can use the method in the model to create your own function.

- Reverse accessors: what allows you to access relatinoship in reverse. 
- Thanks to Django
    - You can grab a room
    - do Room.owner - django gives an user object. 
    - room = Room.objects.get(pk=1)
    - how many rooms do you have from the owner's point of view.

*How can you rever access?*
1. filter
```py
# If you use __ with the forign key, you can just access to items or properties of foreign keys. 
Room.objects.filter(owner__username='nomadcoders')
<Query>
```

user.rooms
user.reviews
user.wishlists

- This is possible after you change one thing from the console. 

*How do you access using reverse accessor?*

```
from users.models import User
me = User.object.get(pk=1)

```

- dir(): It is useful because you can see all properties and methods. 
- There are many _set

- _sets are reverse accessor. 
```py
me.room_set
me.room_set.all()
# YOu can all the rooms created by that user. 
```

category.room_set.all()
Django gives _set option to reverse access. 

As of now, you have two options to access. 
1. user.room
2. user.room_set.all()

In order to do #1, you have to set up special keyword inside the models.py

```py
owner = models.ForeignKey(
    "users.User",
    on_delete=moidels.CASCADE,
    related_name="rooms",
)
```
- speak outloud when you are confused about the relationship. 

Recap:

1. Foreign key
2. 

# Power Admin

- We are going to learn how to create a search box, action and filte.r 

- We can get review average when I am looking at the room. 
- We know how to run a function in admin panel . 
- In admin.py, you can view total_amenities and you can count
```py
def total_amenities(room):
    return room.amenities.count()
```

- If you are going to use in the admin.py
- If you want to use anywhere, you put it in the model.py

```py
def rating(room):
    # There are review model that are pointing to rooms. We can access using a reverse accessor. 
    return room.reviews.count()
    if count == 0:
        return "No Reviews"
    else:
        total_rating = 0
        for review in room.reviews.all():
            total_rating += review.rating
            # two decimal spaces
        return (total_rating / count, 2)
 
```

- You can optimize the lazy loading by getting specific values you want

```py
for review in room.reviews.all().values("rating"):
    # because you changed to bring only values, it will return a dictionary.
    total_rating += review["rating"]
return round(total_rating /count, 2)
```

## Search Fields
- Search room based on the username or the owner of the room.

*How do you create a search bar in the admin console?*
In admin.py,

You add below:
```py
search_fields = (
    "name",
    "price"
)

```
- This will create a search bar that search by fields listed inside the var.

- ^name: start of the name.
- owner__username: you can search by owner username
- =owner__username: search exact word.

*How do you add an action?*

- When you delete, ondelete. It tells you what will be deleted. All you have to do is to create admin.action. 
- In admin.py

```py
from .models import Room, Amenity

@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, requset, querySet):
    # request: request object is about who is calling this action. We can build an admin panel that only username with admin can check. 
    # queryset: the least of all the object that you selected. You will get all the objectsets that you selected.
    for room in rooms.all():
        print(room)
        room.price=0
        room.save()
  
```

*Actions are useful!*
- You can create excel export
- Owner - modify data 

## Custom Filter

- list_filter: fields
- You can filter by foreign keys. 

*How do you create a filter that filter by the foreign key.*


```py
# filter review by the category of room.
# filter by the host of the user.
list_filter = (
    "rating",
    "user__is_host",
    "room__category"
    )
    
```

```py
# Custom user code
from django.contrib.admin import SimpleListFilter


class PopularityFilter(SimpleListFilter):
    title = "popularity"

    parameter_name = "popular"

    def lookups(self, request, model_admin):
        return [("good", "Good(>3)"), ("bad", "Bad(<3)"), ("neutral", "Neutral(=3)")]

    def queryset(self, request, reviews):
        param = self.value()
        match = {
            "good": reviews.filter(rating__gt=3),
            "bad": reviews.filter(rating__lt=3),
            "neutral": reviews.filter(rating__exact=3),
        }
        return match.get(param, reviews)
```

- We can create a filter that has good, awesome, etc keywords. 
- 
```py
class WordFilter(admin.SimpleListFilter):
title = "Fliter By Good & Bad Review"

parameter_name = "positive"


# querySet will return the filter object. 
def lookups(self, request, model_admin):
    return [
        # Second part of a tuple will pop up in the filter.
    ("good", "Good"),
    ("bad", "Bad"),
    ("mediocre", "Mediocre"),
    ]

def queryset(self, request, reviews):
    # Read URL value and extract it.
    word = self.value()
    if word == "good":
    return reviews.filter(rating__gt=3)
    elif word == "bad":
    return reviews.filter(rating__lt=3)
    elif word == "mediocre":
    return reviews.filter(rating__exact=3)
    else:
    return reviews
```

Recap:

- Search fields: by deafult you search looking a contain lookup, you can start lookup with ^ and equal with =.
- Build actions: you create a function decorated by descriptions
    - takes three argument. 
    - last one is what is selected. 
    - You can put that function in the method that you are going to create. 
- You go to review
- Custom filter. 
    - simpleListfilter
    - the word will show in the url. 
    - lookup is the one that should return
    - queryset method: returns filter review.
    - 

# URL and Views

- There are ways to create a template in Django. 
- 99% of the flask is the same. 
- 

Steps:
1. Go to Config/urls.py
2. Views.py is a function that you want to run when the user goes to a specific URL. 
3. views.py: no body looks at it intently for the change. 

urls.py
```py
from django.contrib import render
from django.urls import path
from room import views as room_views
from users import views as users_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # respond with views.say_hello function when user calls this path.
    path("rooms", views.say_hello),
]

views.py
```py
from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse("hello!")
```

*How do you create separate urls in apps?*

- Think about the future. You will have
/rooms
/rooms/1
/rooms/1/edit
/rooms/1/delete
/users
/users/1
/users/1/edit
/users/create-account
etc......

- You don't want to put all these routes in one url.py file. This will make it really confusing. 

Steps:
- Create urls.py inside the app.
urls.py
```py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.say_hello),
]

```
- Create a route to the url of an app from config url.
```py
from django.contrib import admin
from django.urls import path, include
from rooms import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("rooms/", include("rooms.urls"),
]
```

- Move the definition of urls. 
- You make a reference to the app urls.py
- app/urls.py will create a default route ""
- make it execute app.views.py

*How do you render http template in Django?*

*how do you accept urls with variables in them?*

views.py
```py
from django.shortcuts import render
from django.http import HttpResponse

def see_all_rooms(request):
    return HttpResponse("see all rooms")

# take one argument (keyword)
def see_one_room(request, room_id):
    return HttpResponse("see one room")
    # Alternatively you can do this to view room_id. return HttpREsponse (f"see one room with {room_id")

```

urls.py
```py
from django urls import path
from .import views

urlpatterns = [
    path("", views.see_all_rooms),
    # Use less than and greater than; write type of the parameter that you want to receive.
    path("<int:room_id>", views.see_one_room),

]
```

- As a result, you can have many rooms with different id
rooms/1, rooms/2

- you can also make it receive string as well. 

```py
    path("<str:room_name>", views.s)
```

- You can put more than one variables too. 

urls.py
```py
urlpatterns = [
    path("<int:room_id>/<str:room_name>", views.see)
]
```

views.py
```
def see_one_room(request, room_id, room_name):
    return HttpResponse(f"see room with id: {room_id}")
```

## render

- Get all the room from db and display on the page.

```py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

def see_all_rooms(request):
    # Get all rooms from the DB.
    rooms = Room.objects.all()
    return render(request, "all_rooms.html, 
    {
        "rooms": rooms, 
        "title": "Hello! this title comes from django!",
    },
    
    # Third argument is the context data the data that you are going to send.
```

- The template should be in the default location. 
- Django is configured to look at the template in the application folder. 
- app folder/templates/<template>
- 

On the template

.html
```html
<h1>{{title}}</h1>
```

## Django Template

- We searched all the room and created a template to display data. 
- Django can display data with the for..in 
```py
# Assume that there is a context data called "rooms"
<ul>
{% for room in rooms%}
    <li>{{room.name}}</li>
{% endfor %}
</ul>
```

- Go back to your room model and you have amenities. You can access the relationships. 

- rooms.amenities.

```py
<ul>
{% for room in rooms%}
    <li>{{room.name}}</li>
    {% for amenity in room.amenities.all %}
        <span>{{amenity.name}}</span>
    {% endfor%}
{% endfor %}
</ul>
```

- How do I create a route to each room?

```py
<li><a href="/room/{{room.pk}}>link</a>
# this will go and go to room/1 with the pk data included.
```

## DoesNotExist

- When you search the room, you can do that.
views.py
```py
def see_one_room(request, room_pk):
    try:
        room = Room.objects.get(pk=room_pk)
        return render(request, "room_detail.html", 
        {
            "room":room,
        })
    except Room.DoesNotExist
```

template:
```html
{% if not not_found %}
    <h1>{{room.name}}</h1>
    <h2>{{room.country}}/{{room.city}}</h2>
    <h4>{{room.price}}</h4>
{% else %}
    <h1> 404 not found</h1>
{% endif %}

```

*Why not do template?*

- Django is good at creating a dynamic HTML. 
- It is hard to create a dynamic website with Django. 
- Many website is good. 
- But some things are not good enought to create super dynamic. 
- It's very hard to create a dynamic - loading - notification - everything. You have to use ReactJS. 
- We are going to use Django as API. JSON API and GraphQL API. 
- The industry wants to use Django as a backend and ReactJS as the front end. 
- We can use DJango REST Framework that allows us to build API. 


# Django REST framework

- It saves so much time and there are so much shortcuts. 
- Django framework - industry standard. 
- We are going to isntall it and what is it and how does it differnent from rendering a template. 
- Installation part always use pip but we use poetry. 

*How do you install Django REST framework?*

```py
poetry add djangorestframework. 
```
- We create an additional app in seeting.py as "THIRD_PARTY_APP"
- Django is going to look for INSTALLED_APPS. 

*What is the point of using API?*
- iNSTEAD of giving the user HTML, we give JSON. 
- JSON: a format to send code or data. 
- ReactJS is going to take the JSON and make the UI for you. 
- Django will not go to /room directly but the front end will request data from the server and it is going to show data in a beautiful way. 
- Watch Rest API on youtube.
    - We drop CRUD in url and use HTTP method. 
    - Verb: HTTP method
    - Noun: url
    - POST URL. 
    - DELETE URL
    - GET URL

# JsonResponse

- Category: One model
- We have rooms and experiences. 
- You see categories: Chatting room and other can be in one appliccation. 
- 

/categories - shows a list of all categoreis. 
/categories/1 - 

GET - give me. 
POST - send data to the server. 

In the real world, you are going to have GET AND POST. 
Tiny spoiler of how many URL we are going to build. 

- Django REST doesn't change that much. 
- urlpatterns = [

]
- Create a path; When somebody goes to /category. 
- We have to handle it from urls.py. 
- Create a view

```py
from django.http import JsonResponse
from .models import Category

def categories(result):
    all_categories = Category.objects
    return JsonResponse({"ok": True, 
    
    })


```
Google chrome - install JSON viewer. 

- We can't do 
"categories": all_categories,

- QuerySet is not JSON serializable. 
- We can't translate QuerySet to JSON
- QuerySet is a python object. 
- 

*How do you fix "type QuerySet is not JSON serializable*

- How do you translate QuerySet to 
- Django Serializaing Django 
- Format: XML, JSON 

- Manual way, Django serializer

Steps:
1. Import Django serializer. 
2. Change the view.py

```py
def categories(request):
    all_categories = Category.objects.all()
    return JsonResponse(
        {
            "ok":True
            "categories": serializers.serialize("json",
            all_categories),
        }
    )
```

- This is not good because it looks bad and it is displaying all data. We maybe want to hide some data. 
- We use decorator
- We are going to decorate this function with REST framework decorator. 
- 

*How do you create a decorator?*

```py
from rest_framework.decorator import api_view
from rest_framework.response import Response
from .models import Category

@api_view()
def categories(request):
    return Response(
        {
            "ok":True,
        }
    )


```

- The moment you use django REST framework, it gives you all the things that you need to know status code, method, url that you are requesting, the method that you are requesting. 
- Your user is going to see the simple version but we as a developer will see visualizer. 
- Categories: cateogry.objects.all()
- When you refresh you still have the error. 

*How do you fix the issue with the django REST framework?*

- We are going to see a serializer with the Django framework. We are going to look at the serializer. 
- We are going to create a serializer. 
- The translator is called a serializer. 
- We are going to choose how we are going to serialize. 

*How do you create a serializer?*
Steps:
1. Create a serializer.py in the app. 

```py
from rest_framework import serializers
from .serializers import CategorySerializer

class CategorySerializer(serializers.Serializer):
    name = serializer.CharField(required=True)
    kind = serializer.CharField()


```

- Category Serializer only knows how to translate two categories. 
- Serializer is now receiving Django model and translate them in JSON. 
- We have to repeat ourselves for every fields. 

pk = serializer.IntegerField()

Summary:

views.py
```py
serializer = CategorySerializer(all_categories, many=True)
return Respose(
    {
        "ok": True,
        "categories": serializer.data,
    }
)
```

Views > Serializer > return the serialized data. 

## POST requests

GET REQUEST:

urls.py
```py
urlpatterns = [
    path("", views.categories),
    path("<int:pk>", views.category)
]

```
views.py
```py
@api_view()
# receive a parameter named pk
def category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)
    return Response()
```

POST REQUEST:

- Django will reject different type of request if not allowed. 

*How do we allow certain type of requests?*
```py
# Allow both GET and POST method.
@api_view(["GET", "POST"])
def categories(requset):

    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        return Response({"created": True})

```

- if you want the user to send category or a name, you can do that. 
- We are going to print in the data. 
- We do not always trust the user. We need to validate data that the user is trying to modify. 
- The serializer is what you use to translate from Django to user word. Serializer also helps us to take data nad turn it into django object that we can put int he object.