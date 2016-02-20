from ..selenium_page_objects.pages import LoginPage

class ExpensesMonthPage(LoginPage):
    
    def __init__(self,*args,**kwargs):
        self.page_id = 'expenses_month'
        url = '/expenses/'
        super(ExpensesMonthPage,self).__init__(url=url,*args,**kwargs)
        