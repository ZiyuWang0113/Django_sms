from django.db import models


# Create your models her
class Customer(models.Model):
    name = models.CharField(max_length=200)

    phone = models.CharField(max_length=200)

    address = models.CharField(max_length=200)