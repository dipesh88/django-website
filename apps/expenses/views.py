from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.core.urlresolvers import reverse

import datetime

from .models import Expense
from .forms import ExpenseOwnerForm,ExpenseApproveForm

class MainExpensesRedirectView(generic.RedirectView):
    
    def get_redirect_url(self,*arg,**kwargs):
        
        n = datetime.date.today()
        return reverse("expenses:monthly_all",kwargs={'month':n.month,'year':n.year})
        
 

class MonthlyExpensesBaseView(generic.ListView):
    
    model = Expense
    template_name = 'expenses/expenses_month.html'
    
    def get_queryset(self):
        
        return Expense.monthly_expenses.by_month(month=int(self.kwargs['month']),
                                                       year=int(self.kwargs['year'])).filter(account=self.request.user.account)
    
class MonthlyExpensesAllView(MonthlyExpensesBaseView):
    
    def get_queryset(self):
        
        self.approved = self.request.GET.get('approved','all')
        assert self.approved in ['all','yes','no']        
        queryset = super(MonthlyExpensesAllView,self).get_queryset()
        if self.approved != 'all':
            queryset = queryset.filter(is_approved=(self.approved=='yes'))
        return queryset.all()
    
    def get_context_data(self,*args,**kwargs):

        context = super(MonthlyExpensesAllView,self).get_context_data(*args,**kwargs)
        context['approved'] =  {'all':'All','yes': 'Approved','no':'Not Approved'}[self.approved]
        return dict(context,**self.kwargs)    
    
class MonthlyExpensesMyView(MonthlyExpensesBaseView):
    
    def get_queryset(self):
        
        queryset = super(MonthlyExpensesMyView,self).get_queryset()
        return queryset.filter(owner=self.request.user)
    
class MonthlyExpensesDivorceeView(MonthlyExpensesBaseView):
    
    def get_queryset(self):
        
        queryset = super(MonthlyExpensesDivorceeView,self).get_queryset()
        return queryset.filter(owner=self.request.user.divorcee)
    
    


class ApproveExpenseView(generic.UpdateView):
    
    template_name = "expenses/expense_approve.html"
    model = Expense
    context_object_name = "expense"
    form_class = ExpenseApproveForm
    
    def get_object(self):
        
        if hasattr(self,"object"):
            return self.object
        
        object =  get_object_or_404(Expense,pk=int(self.kwargs['pk']),
                                    account=self.request.user.account)
        return object
    
    def get(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        if self.object.owner != request.user and  self.object.can_update():
            return super(ApproveExpenseView, self).get(request, *args, **kwargs)
        else:
            return redirect(self.object.get_absolute_url()) 

class EditExpenseView(generic.UpdateView):
    
    template_name = "expenses/expense_edit.html"
    model = Expense
    form_class = ExpenseOwnerForm
    
    def get_object(self):
        
        if hasattr(self,"object"):
            return self.object
        
        object =  get_object_or_404(Expense,pk=int(self.kwargs['pk']),
                                    account=self.request.user.account)
        return object
    
    def get(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        expense = self.object
        if expense.owner == request.user and not(expense.is_approved) and expense.can_update() :
            return super(EditExpenseView, self).get(request, *args, **kwargs)
        else:
            return redirect(self.object.get_absolute_url())        
        
    
class ExpenseView(generic.DetailView):
    
    template_name = "expenses/expense_details.html"
    context_object_name = "expense"
    form_class = ExpenseOwnerForm
    
    def get_object(self):
               
        object =  get_object_or_404(Expense,pk=int(self.kwargs['pk']),
                                    account=self.request.user.account)
        return object
    
    
class AddExpenseView(generic.CreateView):
    
    model = Expense
    form_class = ExpenseOwnerForm
    template_name = "expenses/expense_add.html"
    success_url = "/"
    
    n = datetime.datetime.now()
    initial = {'date_purchased':n,
               'month_balanced':n.month,
               'year_balanced':n.year,
               'expense_divorcee_participate':50
               }    
    
    
    def form_valid(self, form):
        
        self.object = form.save(commit=False)
        self.object.owner = self.request.user        
        return super(AddExpenseView,self).form_valid(form)
        
        
    
     
     