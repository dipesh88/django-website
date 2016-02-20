import os
import unittest
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_repo.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "site_repo.settings"   

from site_repo.tests.selenium_page_objects.helpers import custom_test_sort
from site_repo.tests.selenium_site.test_case import SeleniumWebTestCaseWithData

from site_repo.tests.load_data import data1
from site_repo.tests.selenium_site import actions
from site_repo.tests.selenium_site import login_pages

class ExpenseTest(SeleniumWebTestCaseWithData):
    
    initial_users = data1.Lusers
    initial_expenses = data1.Dexpenses   
        
    def test_edit_expense(self):
        action = actions.SignInHomePageAction()
        self.browser = action.run(browser=self.browser,username='john',password='123456')
        exp_month = login_pages.ExpensesMonthPage(browser=self.browser)
        exp_month.expenses = 2
        
       
    
    def test_add_expense(self):
        print "add expense"
        
        
if __name__ == '__main__':     
    from site_repo.tests.selenium_site.helpers import set_env
    set_env()
    Ltests = ['test_edit_expense','test_add_expense']
    unittest.TestLoader.sortTestMethodsUsing = custom_test_sort(Ltests)
    unittest.main()