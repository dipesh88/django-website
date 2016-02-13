from django.contrib.auth import update_session_auth_hash
from django.core.urlresolvers import reverse,reverse_lazy
from django.shortcuts import render
from django.views import generic

from . import forms

class UserSettingsView(generic.FormView):
    
    template_name = "users/user_settings.html"
    form_class = forms.UserSettingsForm
    success_url = reverse_lazy("expenses:main_redirect")
    
    def get_form_kwargs(self,*args,**kwargs):
        
        kwargs = super(UserSettingsView,self).get_form_kwargs(*args,**kwargs)
        kwargs['label_suffix'] = ""
        return kwargs
        
    def get_initial(self,*args,**kwargs):
        
        user = self.request.user
        self.initial = {'send_mail_when_divorcee_approve':user.settings.send_mail_when_divorcee_approve,
                        'send_mail_when_divorcee_balance':user.settings.send_mail_when_divorcee_balance,
                        'base_divorcee_participate':user.settings.base_divorcee_participate}
    
        return super(UserSettingsView,self).get_initial() 
    
    
    def form_valid(self, form):
        
        password_changed = form.save(self.request.user)
        if password_changed:
            update_session_auth_hash(self.request,self.request.user)
        
        return super(UserSettingsView,self).form_valid(form)
    
    
               
               
    
