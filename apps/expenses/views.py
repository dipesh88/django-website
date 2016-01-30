from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic

import datetime

from .models import Expense
from .forms import ExpenseOwnerForm


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
        if not self.object.can_update():
            return redirect(self.object.get_absolute_url())        
        
        return super(EditExpenseView, self).get(request, *args, **kwargs)
    
    
    
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
    initial={'date_purchased':n,
             'month_balanced':n.month,
             'year_balanced':n.year,
             'expense_divorcee_participate':50
             }    
    
    
    def form_valid(self, form):
        
        self.object = form.save(commit=False)
        self.object.owner = self.request.user        
        return super(AddExpenseView,self).form_valid(form)
        
        
    
     
     