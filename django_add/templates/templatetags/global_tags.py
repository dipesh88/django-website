import re
from django import template

register = template.Library()
regex_page = re.compile("page=[0-9]+")

@register.filter
def intmonth(value):
    
    try:
        return ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][int(value)-1]
    except:
        return value
    
@register.filter
def currencyformat(value):
    return '{:0,}'.format(int(round(value)))


@register.filter
def striftrue(value,arg):
    """ only for strict boolean, will not convert a True/False typecast"""
    return arg if  value is True else ""

@register.filter
def add_page_arg(url,page_index):
    
    if regex_page.search(url) != None:
        return regex_page.sub("page=%s"%page_index,url)
    else:
        url_base = "%s&&page=%s" if "?" in url else "%s?page=%s"
        return url_base%(url,page_index,)

   
    
    


