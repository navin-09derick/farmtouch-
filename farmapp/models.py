from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product1(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='products/')
    page = models.IntegerField()
    outofstock = models.BooleanField(default=False)


class Sellproduct(models.Model):
    name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    location = models.CharField(max_length=1000)
    quantity = models.PositiveIntegerField()
    date = models.DateField()
    phone_number= models.IntegerField()
    def __str__(self):
        return self.name
  