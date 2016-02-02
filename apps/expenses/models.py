from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from site_repo.django_add.validators import verify_month_int

from ..accounts.models import Account
from ..accounts.API import get_account_by_user

class MonthlyExpensesManager(models.Manager):
    
    def by_month(self,month,year):
        
        queryset = super(MonthlyExpensesManager,self).get_queryset()
        return queryset.filter(month_balanced=month,year_balanced=year)
    
class Objects(models.Manager):
    pass
    


class Expense(models.Model):

    date_entered = models.DateTimeField(auto_now_add=True)
    date_purchased = models.DateField()
    month_balanced = models.IntegerField(validators=[verify_month_int])
    year_balanced = models.IntegerField()

    owner = models.ForeignKey(User,related_name='expenses')
    account = models.ForeignKey(Account,related_name='expenses',blank=True,null=True)

    expense_sum = models.FloatField()
    expense_divorcee_participate = models.IntegerField(validators=[MinValueValidator(0),
                                                                MaxValueValidator(100)])
                                                                   
    desc = models.CharField(max_length=512)
    slug = models.SlugField(max_length=128,blank=True)
    place_of_purchase = models.CharField(max_length=512)
    notes = models.CharField(max_length=1024,blank=True)

    is_approved = models.BooleanField(default=False)

    monthly_expenses = MonthlyExpensesManager()
    objects = Objects() # not avialable w/o explicit assignment when other manager assigned
    

    def get_absolute_url(self):
        
        return reverse('expenses:details',args=[str(self.pk),self.slug])
    
    def get_edit_url(self):
            
            return reverse('expenses:edit',args=[str(self.pk),self.slug])
        
    def get_approve_url(self):
            
            return reverse('expenses:approve',args=[str(self.pk),self.slug])    
        
        
    def save(self,*args,**kwargs):

        self.slug = slugify(self.desc)
        try:
            self.account = self.owner.account
        except:
            self.account = get_account_by_user(self.owner)
        if not self.can_update():
            raise ValidationError(message="Account is balanced for this month, can't add or update expenses")        
        
        super(Expense,self).save(*args,**kwargs)
        
    def can_update(self):
        
        return not (self.account.locked_expenses(month=self.month_balanced,
                                               year=self.year_balanced))



