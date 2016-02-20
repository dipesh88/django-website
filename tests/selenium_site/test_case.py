from site_repo.tests.selenium_page_objects.test_case import SeleniumWebTestCaseBase
from site_repo.tests.load_data import helpers


class SeleniumWebTestCaseWithData(SeleniumWebTestCaseBase):
    
    initial_users = None
    initial_expenses = None
    send_emails = False
    
    def setUpTestData(self):
        
        helpers.add_users(self.initial_users,self.send_emails)
        helpers.add_expenses(self.initial_expenses)
        
        
        
        
        
        
        
    
    