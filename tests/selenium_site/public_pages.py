from ..selenium_page_objects.pages import WebPageBase
from . import forms

class PublicPage(WebPageBase):
    """ not login required"""
        
    def __init__(self,*args,**kwargs):
        
        super(PublicPage,self).__init__(*args,**kwargs)


class HomePage(PublicPage):
    
    def __init__(self,*args,**kwargs):
        self.page_id = 'home_page'
        url = '/'
        super(HomePage,self).__init__(url=url,*args,**kwargs)
        self.form = forms.HomePageSignInForm(browser=self.browser)
        return
        
    def sign_in(self,username,password):
        
        self.browser.execute_script("$('#show_sign_in_intro').click()")
        self.form.set_input_text({'username':username,'password':password})
        self.form.submit()
        return self.browser
        
        
    
        
    