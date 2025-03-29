#Create a custom user model that extends Django’s AbstractUser, 
# adding fields such as bio, profile_picture, 
# and followers (a ManyToMany field referencing itself, symmetrical=False).

from django.contrib.auth.models import AbstractUser
from django.db import models

class Followers(models.Model):
    pass

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=255)
    profile_picture = models.ImageField(upload_to='pics/')
    followers = models.ManyToManyField('self',related_name='followed_by', symmetrical=False, blank=True)
    following = models.ManyToManyField('self', related_name= 'followers')




# Create your models here.
