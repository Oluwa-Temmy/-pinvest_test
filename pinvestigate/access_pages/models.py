from django.db import models

# Create your models here.
class Example(models.Model):
    title = models.CharField(max_length=45)
    body = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)