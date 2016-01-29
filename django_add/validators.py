from django.core.exceptions import ValidationError
from django.http import Http404
def verify_month_int(value):
    
    if value not in range(1,12):
        raise ValidationError(message='Please select a month 1-12')
    
