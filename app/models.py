from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name