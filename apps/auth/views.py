from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from ...cache.API import clear_user_cache
from . import forms

class SignUpView(generic.edit.FormView):
    
    form_class = forms.SignupForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy("expenses:main_redirect")
    
    
    def form_valid(self, form):
        
        user = form.save()
        login(self.request,user)
        return super(SignUpView,self).form_valid(form)
    
    
class LoginView(generic.edit.FormView):
    
    form_class = AuthenticationForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy("expenses:main_redirect")
    
    def form_valid(self, form):
        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)   
        

def logout_user(request):
    
    clear_user_cache(request.user)
    logout(request)
    return HttpResponseRedirect("/login/")
    
    
    