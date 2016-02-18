import datetime

from . import selenium_settings

def verify_browser(browser):
    
    for check_browser in selenium_settings.WEBDRIVERS.values():
        
        if isinstance(browser,check_browser):
            return True
        
    return False
    
    

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
