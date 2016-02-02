from django import template

register = template.Library()

@register.filter
def intmonth(value):
    
    try:
        return ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][value-1]
    except:
        return value
    
@register.filter
def currencyformat(value):
    return '{:0,}'.format(int(round(value)))


@register.filter
def striftrue(value,arg):
    """ only for strict boolean, will not convert a True/False typecast"""
    return arg if  value is True else ""

   
    
    


