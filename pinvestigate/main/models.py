from django.db import models

# Create your models here.
class Crimminal(models.Model):
    crimminal_firstname = models.CharField(max_length=128)
    crimminal_lastname = models.CharField(max_length=128)

    crimminal_address = models.SlugField(max_length=132)
    
    crimminal_offenses = models.PositiveIntegerField
    crimminal_resolve = models.BooleanField(default=False)

    def __str__(self):
        return self.name

