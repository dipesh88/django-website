from django.test import TestCase
from .driver import SeleniumDriver

class SeleniumWebTestCase(TestCase):
    
    fixtures = []
    
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumDriver()
        cls.browser = cls.driver.browser
        super(SeleniumWebTestCase, cls).setUpClass()
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super(SeleniumWebTestCase,cls).tearDownClass()
        
    
        
    
        
        
        
        