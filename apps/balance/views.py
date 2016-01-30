from django.shortcuts import render
from django.views import generic

from .models import MonthlyBalance

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
                