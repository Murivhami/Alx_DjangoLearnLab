#First model for api app.

from django.db import models
class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharFielf(max_length=200)
  
# Create your models here.
