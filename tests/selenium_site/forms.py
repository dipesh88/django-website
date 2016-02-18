from ..selenium_page_objects import forms_base

class HomePageSignInForm(forms_base.WebFormById):
    
    def __init__(self,browser):
        
        self.element_id = "home_page_sign_in_form"
        super(HomePageSignInForm,self).__init__(self,browser)


    
    