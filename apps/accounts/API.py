from .models import Account

def get_account_by_user(user):
    
    try:
        return Account.objects.get(divorcee1_id=user.id)
    except:
        return Account.objects.get(divorcee2_id=user.id)