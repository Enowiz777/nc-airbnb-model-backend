from django.contrib import admin
from .models import House

# Register your models here.
# Create an admin panel for a House model.
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass
