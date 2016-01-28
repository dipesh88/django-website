from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    
    divorcee1 = models.ForeignKey(User,related_name="divorcee1_account")
    divorcee2 = models.ForeignKey(User,related_name="divorcee2_account",blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    