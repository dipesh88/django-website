from ..selenium_page_objects.pages import PublicPage
from . import forms

class HomePage(PublicPage):
    
    def __init__(self,*args,**kwargs):
        self.page_id = 'home_page'
        url = '/'
        super(HomePage,self).__init__(url=url,*args,**kwargs)
        sign_in_form = forms.HomePageSignInForm(browser=self.browser)
        sign_in_form.get_form_element()
        self.forms = {'sign_in':sign_in_form}
        return
        
    def sign_in(self,username,password):
        
        self.browser.execute_script("$('#show_sign_in_intro').click()")
        self.forms['sign_in'].set_input_text({'username':username,'password':password})
        self.forms['sign_in'].submit()
        
        
    
        
    