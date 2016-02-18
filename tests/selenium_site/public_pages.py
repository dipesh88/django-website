from ..selenium_page_objects.pages import PublicPage
from . import forms

class HomePage(PublicPage):
    
    def __init__(self,browser):
        self.page_id = 'home_page'
        url = '/'
        super(HomePage,self).__init__(browser=browser,url=url)
        self.forms = {'sign_in':forms.HomePageSignInForm}
        
    def sign_in(self,username,password):
        
        self.browser.execute_script("$('#show_sign_in_intro').click()")    

        
    
        
    