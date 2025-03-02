
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=2020)

    def __str__(self):
        return f"'{self.title}' by {self.author}"

#CustomUser

from django.contrib.auth.models import AbstractUser
from django.db.models import DateField
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='photos/', null=True, blank=True )

