from django.db import models

# Create your models here.

class Manager(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    productmanager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    def __str__(self):
         return self.name
