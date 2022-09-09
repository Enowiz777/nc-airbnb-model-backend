from django.contrib import admin
from .models import House

# Register your models called House in the admin panel.
@admin.register(House)

# Class inherit everything from the ModelAdmin.
# Create a class called HouseAdmin
# HouseAdmin inherits everything from admin panel for your model.
# ModelAdmin is in admin panel.
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
    
