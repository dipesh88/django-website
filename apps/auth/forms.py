from django import forms
from django.contrib.auth.forms import UserCreationForm

from ...lang import forms_helptext
from ..users import API as API_USERS

class SignupForm(forms.Form):
    
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32,widget=forms.PasswordInput)
    email = forms.EmailField()
    account_code = forms.CharField(max_length=36,min_length=36,required=False,
                                   help_text=forms_helptext.signup_account_code)
    
        
    def save(self):
           
        user = API_USERS.register_user(username=self.cleaned_data['username'],
                                       email=self.cleaned_data['email'],
                                       password=self.cleaned_data['password'],
                                       account_code=self.cleaned_data['account_code']) 
        
        return user
        
        
        
    
    