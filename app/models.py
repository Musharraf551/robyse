from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ValidationError

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
    
class Booking(models.Model):
    instance = models.ForeignKey('Model1', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')
    name = models.CharField(max_length=255)  # Auto-filled
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Auto-filled
    date = models.DateField()
    time_slot = models.CharField(max_length=50)
    number_of_people = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking for {self.name} on {self.date}"

def rating_len(value):
    if value > 5 or value < 1:
        raise ValidationError('rating should be in the range of 1-5')  
    
class Review(models.Model):
    instance = models.ForeignKey('Model1', on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)  # Auto-filled
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback')
    # reviewer_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    rating = models.IntegerField(validators=[rating_len])

    def __str__(self):
        return f"Review by {self.reviewer_name} for {self.name.name}"
    
class About(models.Model):
    sitename = models.CharField(max_length=100)
    about = models.CharField(max_length=255)
    
class Staffs(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='images/')
    