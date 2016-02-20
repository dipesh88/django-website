import os
import unittest
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_repo.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "site_repo.settings"   

from site_repo.tests.selenium_site.test_case import SeleniumWebTestCaseWithData


class MyTest(SeleniumWebTestCaseWithData):
    
    initial_users = {}
    initial_expenses = {}       
        
    def __init__(self, methodName='runTest'):
        self.setUpTestData()
        super(MyTest,self).__init__(methodName)
    
    def test_something(self):
        self.assertEqual('foo','foo')
        self.assertNotEqual('foo','baz')
        
        
if __name__ == '__main__':     
    from site_repo.tests.selenium_site.helpers import set_env
    set_env()
    unittest.main()