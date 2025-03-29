from django.db import models
from django.conf import settings
import datetime
from django.contrib.contenttypes.fields import GenericForeignKey

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    verb = models.TextField()
    target = GenericForeignKey(object)
    timestamp = models.DateTimeField

# Create your models here.
