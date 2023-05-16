from django.db import models

# Create your models here.
class Crimminal(models.Model):
    crimminal_firstname = models.CharField(max_length=128)
    crimminal_lastname = models.CharField(max_length=128)
    

