from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django.template.defaultfilters import slugify

from site_repo.django_add.validators import verify_month_int

from ..accounts.models import Account


class Expense(models.Model):

    date_entered = models.DateTimeField(auto_now_add=True)
    date_purchased = models.DateField()
    month_balanced = models.IntegerField(validators=[verify_month_int])
    year_balanced = models.IntegerField()

    owner = models.ForeignKey(User,related_name='expenses')
    account = models.ForeignKey(Account,related_name='expenses')

    expense_sum = models.FloatField()
    expense_divorcee_participate = models.IntegerField(validators=[MinValueValidator(0),
                                                                MaxValueValidator(100)])
                                                                   
    desc = models.CharField(max_length=512)
    slug = models.SlugField(max_length=128,blank=True)
    place_of_purchase = models.CharField(max_length=512)
    notes = models.CharField(max_length=1024,blank=True)

    is_approved = models.BooleanField(default=False)


    def save(self,*args,**kwargs):

        self.slug = slugify(self.desc)
        super(Expense,self).save(*args,**kwargs)



