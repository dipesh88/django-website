from django.core.exceptions import ValidationError

def verify_month_int(value):
    
    if value not in range(1,12):
        raise ValidationError(message='Please select a month 1-12')