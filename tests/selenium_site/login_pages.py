from ..selenium_page_objects.pages import LoginPage
from ..selenium_page_objects import elements_base

class ExpensesMonthPage(LoginPage):
    
    _expenses = []
    
    def __init__(self,*args,**kwargs):
        self.page_id = 'expenses_month'
        url = '/expenses/'
        super(ExpensesMonthPage,self).__init__(url=url,*args,**kwargs)
        self._expense_base = elements_base.WebElementByXPath(browser=self.browser)
        self._expense_base.xpath_template = '//*[@id="expenses_table"]/tbody/tr[%s]'
        
    @property
    def expenses(self):    
        return self._expenses
    
    @expenses.setter
    def expenses(self,expenses_on_page):
        self._expenses = []
        for m in range(2,expenses_on_page+2):
            expense = self._expense_base.new_element_by_xpath_template(m)
            self._expenses.append(expense)
            
    
        