from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..accounts.models import Account
from ..expenses.models import Expense

from site_repo.django_add.validators import verify_month_int

class MonthlyBalance(models.Model):
    
    class Meta:
            unique_together =('month_of_balance','year_of_balance','account')  
    
    month_of_balance = models.IntegerField(validators=[verify_month_int])
    year_of_balance = models.IntegerField()
    
    account = models.ForeignKey(Account,related_name="months_balanced")
    
    divorcee1 = models.ForeignKey(User,blank=True,null=True,related_name="divorcee1_balance")
    divorcee2 = models.ForeignKey(User,blank=True,null=True,related_name="divorcee2_balance")
    
    is_balanced = models.BooleanField(default=False)
    
    
@receiver(post_save,sender=Expense)
def first_expense_for_month(*args,**kwargs):
    
    expense = kwargs['instance']
    Dcriteria = {'month_of_balance':expense.month_balanced,
                 'year_of_balance':expense.year_balanced,
                 'account':expense.account}
    try:
        m = MonthlyBalance.objects.get(**Dcriteria)
    except ObjectDoesNotExist:        
        m = MonthlyBalance(**Dcriteria)
        m.save()