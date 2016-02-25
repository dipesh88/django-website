from site_repo.tests.selenium_page_objects import elements_base,exceptions

class ExpenseRowElement(object):
    
    def __init__(self,element_by_xpath):
        
        assert isinstance(element_by_xpath, elements_base.WebElementByXPath)
        self.element = element_by_xpath.element
        self.browser = element_by_xpath.browser
        self.xpath = element_by_xpath.element_xpath
       
    @property 
    def text(self):
        
        return self.element.text
    
    def details(self):
        
        self.element.find_element_by_xpath(self.xpath+"/td[1]/a").click()
        return self.browser
    
    @property
    def approved(self):
        
        try:
            approved_value = self.element.find_element_by_xpath(self.xpath+"/td[6]/input").get_attribute("checked")
        except exceptions.NoSuchElementException:
            approved_value = self.element.find_element_by_xpath(self.xpath+"/td[6]/span").get_attribute("approved")
            
        return approved_value == "true"
    