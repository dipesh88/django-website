from django.contrib.auth.models import User
from django.db import models

class UserSettings(models.Model):
    
    user = models.OneToOneField(User)
    send_mail_when_divorcee_approve = models.BooleanField(default=False)
    send_mail_when_divorcee_balance = models.BooleanField(default=False)
    base_divorcee_participate = models.IntegerField(default=50)
