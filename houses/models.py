from django.db import models

# Create your models here.
# Inherit from Model class - CTRL to view.
class House(models.Model):

    # Convention for Model comment
    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
