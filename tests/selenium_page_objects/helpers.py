import datetime

from . import selenium_settings

def verify_browser(browser):
    
    for check_browser in selenium_settings.WEBDRIVERS.values():
        
        if isinstance(browser,check_browser):
            return True
        
    return False


def is_user_input_field(input_name):
    
    return not (len(input_name) < 1 or input_name in selenium_settings.EXCLUDE_FIELDS)
 
    

def full_url(url):
    
    protocol = 'https' if selenium_settings.USE_HTTPS else 'http'
    u = '{protocol}://{host}{url}'.format(protocol=protocol,host=selenium_settings.HOST,url=url)
    return u

def poll_dom(func,arg,timout):

    start = datetime.datetime.now()
    until = start + datetime.timedelta(0,timout) ## (days,seconds)
    crr = start

    while crr <= until:
        try:
            Lelements = func(arg)
            return Lelements
        except:
            pass

    return[]
