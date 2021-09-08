from django.db import models
from django.db.models.fields import AutoField

# Create your models here.

class Product(models.Model):

    Product_ID = models.AutoField
    Product_Name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=200)
    Product_Date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.Product_Name
