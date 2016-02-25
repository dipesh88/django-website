from ..selenium_page_objects import forms_base

class HomePageSignInForm(forms_base.WebFormById):
    
    def __init__(self,*args,**kwargs):
              
        element_id = "home_page_sign_in_form"
        super(HomePageSignInForm,self).__init__(element_id=element_id,*args,**kwargs)
        

class ExpenseForm(forms_base.WebFormById):
    
    def __init__(self,*args,**kwargs):
        
        element_id = "expense_form"
        super(ExpenseForm,self).__init__(element_id=element_id,*args,**kwargs)
        
class ExpenseDeleteForm(forms_base.WebFormById):
    
    def __init__(self,*args,**kwargs):
        
        element_id = "delete_form"
        super(ExpenseDeleteForm,self).__init__(element_id=element_id,*args,**kwargs)
        
class SignUpForm(forms_base.WebFormById):
    
    def __init__(self,*args,**kwargs):
        
        element_id = "sign_up_form"
        super(SignUpForm,self).__init__(element_id=element_id,*args,**kwargs)


    
    