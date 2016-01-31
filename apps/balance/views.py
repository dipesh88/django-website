import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic

from .models import MonthlyBalance

class MainBalanceRedirectView(generic.RedirectView):
    
    def get_redirect_url(self):
        
        n = datetime.datetime.today()
        return reverse("balance:year",kwargs={'year':n.year})
        


class YearlyMonthBalanceView(generic.ListView):
    
    template_name = 'balance/monthly_balance_year.html'
    
    def get_queryset(self):
        
        queryset = MonthlyBalance.objects.filter(account=self.request.user.account,
                                                 year_of_balance=self.kwargs['year'])
        return queryset


class ClearMonthBalanceView(generic.DetailView):
    
    model = MonthlyBalance
    template_name = 'balance/monthly_balance_details.html'
    context_object_name = 'month_balance'

    def get_object(self):
        
        object =  self.get_queryset().get(account=self.request.user.account,
                                             month_of_balance=int(self.kwargs['month']),
                                             year_of_balance=int(self.kwargs['year']))
        object.me_cleared = object.divorcee_cleared_month(self.request.user)
        object.divorcee_cleared = object.divorcee_cleared_month(self.request.user.divorcee)
        return object
                