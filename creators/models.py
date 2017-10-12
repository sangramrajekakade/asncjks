from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserRegister(models.Model):
    username = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=True)
    email_confirm = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)

  
