from public_pages import HomePage

def sign_in_home_page(browser,username,password):
    
    home_page = HomePage(browser=browser)
    home_page.sign_in(username,password)