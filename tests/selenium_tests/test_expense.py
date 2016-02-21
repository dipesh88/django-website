import os
import unittest
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_repo.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "site_repo.settings"   

from site_repo.tests.selenium_page_objects.helpers import custom_test_sort
from site_repo.tests.selenium_site.test_case import SeleniumWebTestCaseWithData

from site_repo.tests.load_data import data1
from site_repo.tests.selenium_site import actions,helpers
from site_repo.tests.selenium_site import login_pages

class ExpenseTest(SeleniumWebTestCaseWithData):
    
    initial_users = data1.Lusers
    initial_expenses = data1.Dexpenses   
      
    def test_expenses_list(self):
            action = actions.SignInHomePageAction()
            self.browser = action.run(browser=self.browser,username='john',password='123456')
            exp_month = login_pages.ExpensesMonthPage(browser=self.browser,expenses=2)
            self.assertEqual(exp_month.expenses[0].text,
                             helpers.format_today_full('School john 130 50% {today} -'))
            self.assertEqual(exp_month.expenses[1].text,
                                         helpers.format_today_full('Sneakers john 90 50% {today} -'))            
    
    def test_expense_details(self):
        exp_month = login_pages.ExpensesMonthPage(browser=self.browser,expenses=2)
        self.browser = exp_month.expenses[0].details()
        exp_details = login_pages.ExpenseDetailsPage(browser=self.browser)
        Lmodel_html = ['Description School', 'Place of purchase Book Store', 'Purchased by john',
                       helpers.format_today('Date of Purchase {today}'), u'Cost 130.0', u'Divorcee participate % 50', u'Notes']
        self.assertEqual(exp_details.model_html,Lmodel_html)
        
    def test_edit_expense(self):
        pass
        
    def test_add_expense(self):
        pass
        
        
if __name__ == '__main__':     
    from site_repo.tests.selenium_site.helpers import set_env
    set_env()
    Ltests = ['test_expenses_list',
              'test_expense_details',
              'test_edit_expense',
              'test_add_expense']
    unittest.TestLoader.sortTestMethodsUsing = custom_test_sort(Ltests)
    unittest.main()