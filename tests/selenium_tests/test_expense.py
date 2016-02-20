import os
import unittest
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_repo.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "site_repo.settings"   

from site_repo.tests.selenium_page_objects.helpers import custom_test_sort
from site_repo.tests.selenium_site.test_case import SeleniumWebTestCaseWithData


class ExpenseTest(SeleniumWebTestCaseWithData):
    
    initial_users = {}
    initial_expenses = {}       
        
    def __init__(self, methodName='runTest'):
        self.setUpTestData()
        super(ExpenseTest,self).__init__(methodName)
        
    
    def test_edit_expense(self):
        print "edit expense"
    
    def test_add_expense(self):
        print "add expense"
        
        
if __name__ == '__main__':     
    from site_repo.tests.selenium_site.helpers import set_env
    set_env()
    Ltests = ['test_edit_expense','test_add_expense']
    unittest.TestLoader.sortTestMethodsUsing = custom_test_sort(Ltests)
    unittest.main()