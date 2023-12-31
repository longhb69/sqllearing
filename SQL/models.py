from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    user_phone = models.CharField(max_length=100)
    user_country = models.CharField(max_length=100, null=True,blank=True)

    def __str__(self):
        return f"{self.username}"


class SQLTutorial(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    qizanswer = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.title

class Customers(models.Model):
    customerID = models.IntegerField(primary_key=True)
    customerName = models.CharField(max_length=50)
    contactName = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postalCode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

