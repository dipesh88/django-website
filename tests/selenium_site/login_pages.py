from ..selenium_page_objects.pages import LoginPage
from ..selenium_page_objects import elements_base
from . import elements

class ExpenseDetailsPage(LoginPage):
    
    page_id = "expense_details"
    
    @property
    def model_html(self):
        m = self.wrapper.get_html_element_by_id("model_html")
        return m.text.split('\n')[:-1]
    
    
class ExpensesMonthPage(LoginPage):
    
    _expenses = []
    page_id = 'expenses_month'
    
    def __init__(self,*args,**kwargs):

        url = '/expenses/'
        super(ExpensesMonthPage,self).__init__(url=url,*args,**kwargs)
        self._expense_base = elements_base.WebElementByXPath(browser=self.browser)
        self._expense_base.xpath_template = '//*[@id="expenses_table"]/tbody/tr[%s]'
        if kwargs.has_key('expenses'):
            self.expenses = kwargs['expenses']
            
    @property
    def expenses(self):    
        return self._expenses
    
    @expenses.setter
    def expenses(self,expenses_on_page):
        self._expenses = []
        for m in range(2,expenses_on_page+2):
            expense = self._expense_base.new_element_by_xpath_template(m)
            self._expenses.append(elements.ExpenseRowElement(expense))
            
    
        