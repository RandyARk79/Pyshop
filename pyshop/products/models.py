from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField(max_length=10)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2788)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=278)
    discount = models.FloatField(max_length=10)