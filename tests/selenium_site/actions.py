from site_repo.tests.selenium_page_objects.actions import SeleniumWebActionBase

from . import public_pages
from . import login_pages

class SignInHomePageAction(SeleniumWebActionBase):
    
    def action_sign_in_home_page(self,browser,username,password):
    
        home_page = public_pages.HomePage(browser=browser)
        home_page.sign_in(username,password)