import datetime
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
from django.views import generic


from ...lang import balance as lang_balance
from ...utils.misc import last_day_of_prev_month,last_day_of_month

from .helpers import clear_month_balance
from .models import MonthlyBalance

class MainBalanceRedirectView(generic.RedirectView):
    
    def get_redirect_url(self):
        
        n = datetime.datetime.today()
        return reverse("balance:year",kwargs={'year':n.year})
        
class ClearMonthBalanceChangedView(generic.DetailView):     
    
    
    def get(self,request,*args,**kwargs):
        
            cleared = {'cleared':True,'not-cleared':False}[request.GET['changed-to']]
            balance = clear_month_balance(user=request.user,
                                          month=self.kwargs['month'],
                                          year=self.kwargs['year'],
                                          cleared=cleared)
    
            return redirect(balance.get_absolute_url())  
        
            
        
        

class ClearMonthBalanceView(generic.DetailView):
    
    model = MonthlyBalance
    template_name = "balance/monthly_balance_clear.html"
    context_object_name = 'balance'
    
    def get_object(self):
            
            object = MonthlyBalance.balance_aggregate.by_month(user=self.request.user,
                                                               year=self.kwargs['year'],
                                                               month=self.kwargs['month'],
                                                               approved="yes")
            
            L = [object['balance_object'].divorcee1,object['balance_object'].divorcee2]
            me_cleared = lang_balance.cleared if self.request.user in L else lang_balance.not_cleared
            divorcee_cleared = lang_balance.cleared if self.request.user.divorcee in L else lang_balance.not_cleared
            object['user_cleared'] = self.request.user in L
            object['me_cleared'] = me_cleared%self.request.user.username
            object['divorcee_cleared'] = divorcee_cleared%self.request.user.divorcee.username
            
            return object
        
    def get_context_data(self,*args,**kwargs):
            
            context = super(ClearMonthBalanceView,self).get_context_data(*args,**kwargs)
            return dict(context,**self.kwargs)
        

class YearlyMonthBalanceView(generic.ListView):
    
    template_name = 'balance/monthly_balance_year.html'
    
    def get_queryset(self):
        
        self.approved = self.request.GET.get('approved','all')
        assert self.approved in ['all','yes','no']
        queryset = MonthlyBalance.balance_aggregate.by_year(self.request.user,self.kwargs['year'],self.approved)
        return queryset
    
    def get_context_data(self,*args,**kwargs):
        
        context = super(YearlyMonthBalanceView,self).get_context_data(*args,**kwargs)
        context['select_years'] = settings.YEARS_TO_FILTER_ON_GUI
        context['approved'] =  {'all':'All','yes': 'Approved','no':'Not Approved'}[self.approved]
        return dict(context,**self.kwargs)


class MonthBalanceView(generic.DetailView):
    
    model = MonthlyBalance
    template_name = 'balance/monthly_balance_details.html'
    context_object_name = 'balance'

    def get_object(self):
        
        self.approved = self.request.GET.get('approved','all')
        assert self.approved in ['all','yes','no']        
        object = MonthlyBalance.balance_aggregate.by_month(user=self.request.user,
                                                           year=self.kwargs['year'],
                                                           month=self.kwargs['month'],
                                                           approved=self.approved)
        
        L = [object['balance_object'].divorcee1,object['balance_object'].divorcee2]
        me_cleared = lang_balance.cleared if self.request.user in L else lang_balance.not_cleared
        divorcee_cleared = lang_balance.cleared if self.request.user.divorcee in L else lang_balance.not_cleared
        
        object['me_cleared'] = me_cleared%self.request.user.username
        object['divorcee_cleared'] = divorcee_cleared%self.request.user.divorcee.username
        
        return object
    
    def get_context_data(self,*args,**kwargs):
            
            
            context = super(MonthBalanceView,self).get_context_data(*args,**kwargs)
            context['approved'] =  {'all':'All','yes': 'Approved','no':'Not Approved'}[self.approved]
            if last_day_of_month(int(self.kwargs['year']),int(self.kwargs['month'])) <= last_day_of_prev_month():
                context['can_clear'] = True            
            return dict(context,**self.kwargs)    
                