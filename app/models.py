from django.db import models

# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.Category_name
    
class Items(models.Model):
    Item_name = models.CharField(max_length=40)
    
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='items/')
    
    def __str__(self):
        return self.Item_name

