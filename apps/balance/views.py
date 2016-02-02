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
        
        queryset = MonthlyBalance.balance_aggregate.by_year(self.request.user,self.kwargs['year'])
        return queryset


class MonthBalanceView(generic.DetailView):
    
    model = MonthlyBalance
    template_name = 'balance/monthly_balance_details.html'
    context_object_name = 'balance'

    def get_object(self):
        
        object = MonthlyBalance.balance_aggregate.by_month(user=self.request.user,
                                                           year=self.kwargs['year'],month=self.kwargs['month'])
        
        L = [object['balance_object'].divorcee1,object['balance_object'].divorcee2]
        object['me_cleared'],object['divorcee_cleared'] = self.request.user in L,self.request.user.divorcee in L
        
        return object
                