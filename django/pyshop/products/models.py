from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Discount_Offers(models.Model):
    coupon_code = models.CharField(max_length=10)
    discription = models.CharField(max_length=255)
    discount_amount = models.FloatField()