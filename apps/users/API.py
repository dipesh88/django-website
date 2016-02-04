from django.contrib.auth import authenticate
from django.contrib.auth.models  import User
from django.core.exceptions import ValidationError
from ...utils.mail import send_mail_to_user
from ...lang import mail as lang_mail

from ..accounts.models import Account

def register_user(username,email,password,account_code):
    
    account = None
    if len(account_code) > 0:
        try:
            account = Account.objects.get(account_code=account_code)
        except:
            # don't create a user that wants to join an account but provided wrong code
            raise ValidationError(message="No account found for this account code. Please verify that you got the correct code")
   
        
    User.objects.create_user(username=username,email=email,password=password)
    user = authenticate(username=username,password=password)    
    
    if account != None:
        assert account.divorcee1 != None
        assert account.divorcee2 == None
        account.divorcee2 = user
        user.divorcee = account.divorcee1
    else:
        account = Account(divorcee1=user)
        user.divorcee = None
        
    account.save()
    user.account = account
    
    send_mail_to_user(user,**lang_mail.welcome_mail)
    
    return user
    
   