from email.policy import default
from unicodedata import name
from django.db import models

class NewsUnit(models.Model):
    classification = models.CharField(max_length=10,null=False)
    name = models.CharField(max_length=20,null=False)
    title = models.CharField(max_length=50,null=False)
    message = models.TextField(null=False)
    time = models.DateTimeField(null=False)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Product(models.Model):
    pName =  models.CharField(max_length=100, default='')
    pPrice = models.IntegerField(default=0)
    pQty = models.BooleanField(default=False)
    pImage = models.ImageField(upload_to='image/')
    pClass = models.CharField(max_length=20, default='')
    pNew = models.BooleanField(default=False)
    def __str__(self):
        return self.pName
