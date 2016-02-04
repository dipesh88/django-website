from django.conf import settings
from django.core.mail import send_mail


def send_mail_to_user(user,subject,message):
    
    if user.email != None:
        send_mail(subject=subject,
              message=message,
              from_email=settings.FROM_EMAIL,
              recipient_list=[user.email])
              
    return