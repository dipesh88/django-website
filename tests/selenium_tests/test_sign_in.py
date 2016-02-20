import os
import unittest
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_repo.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "site_repo.settings"   

from site_repo.tests.selenium_site.test_case import SeleniumWebTestCaseWithData

from django.contrib.auth import authenticate
from site_repo.tests.load_data import data1
from site_repo.tests.selenium_site import actions
from site_repo.tests.selenium_site.login_pages import ExpensesMonthPage

class SignIn(SeleniumWebTestCaseWithData):
    
    initial_users = data1.Lusers
    initial_expenses = data1.Dexpenses       
        
    def __init__(self, methodName='runTest'):
        self.setUpTestData()
        super(SignIn,self).__init__(methodName)
    
    def test_signin(self):
        u = authenticate(username="john",password="123456")
        assert u != None
        actions.sign_in_home_page(self.browser, "john", "123456")
        ExpensesMonthPage(browser=self.browser)
        
        
if __name__ == '__main__':     
    from site_repo.tests.selenium_site.helpers import set_env
    set_env()
    unittest.main()