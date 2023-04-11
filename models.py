from django.db import models

# Create your models here.
#Creating a database model for item
class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length =200)
    item_description = models.CharField(max_length = 200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default ='https://thumbs.dreamstime.com/b/pizza-rustic-italian-mozzarella-cheese-basil-leaves-35669930.jpg')