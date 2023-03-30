from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

sites = ["https://www.google.com","https://www.python.org","http://aljazeera.net"]

for site in sites:
    driver.get(site)
    print('-------------Title-------------------')
    print(driver.title)
    cookies = driver.get_cookies()
    print('-------------Cookies--------------------')
    for cookie in cookies:
        print(cookie['domain'])
        #print(cookie['name'])
        #print(cookie['value'])
 

#driver.quit()