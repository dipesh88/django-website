from django.contrib.auth.models import User
from django.db import models

from ..accounts.models import Account

from site_repo.django_add.validators import verify_month_int

class MonthlyBalance(models.Model):
    
    month_to_balance = models.IntegerField(validators=[verify_month_int])
    year_to_balance = models.IntegerField()
    
    account = models.ForeignKey(Account,related_name="months_balanced")
    
    divorcee1 = models.ForeignKey(User,blank=True,related_name="divorcee1_balance")
    divorcee2 = models.ForeignKey(User,blank=True,related_name="divorcee2_balance")
    
    is_balanced = models.BooleanField()