import time
import unittest
from site_repo.tests.selenium_page_objects.test_case import SeleniumWebTestCase
from site_repo.tests.selenium_site import actions

class SignIn(SeleniumWebTestCase):
    
    def runTest(self):
        pass
    
    def test_signin(self):
        
        actions.sign_in_home_page(self.browser, "john", "123")
        time.sleep(10)
        
if __name__ == '__main__':
    unittest.main()
        