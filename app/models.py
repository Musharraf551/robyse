from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Model1(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE, related_name='model1_items')
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    location = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name