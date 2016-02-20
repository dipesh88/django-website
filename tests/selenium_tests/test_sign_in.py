import time
import unittest
from site_repo.tests.selenium_site.test_case import SeleniumWebTestCaseWithData
from site_repo.tests.selenium_site import actions
from site_repo.tests.load_data import data1
from django.contrib.auth import authenticate

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
        time.sleep(10)
        
if __name__ == '__main__':
    from site_repo.tests.selenium_site.helpers import set_env
    set_env()
    unittest.main()