from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
from urllib.parse import parse_qs
import re


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome("/usr/bin/chromedriver",chrome_options=chrome_options)

sites = ["http://www.google.com","http://www.python.org","http://aljazeera.net","https://fpt.usmba.ac.ma/new/"]
ID_MIN_LENGTH = 4

for site in sites[3:4]:
    driver.get(site)
    print('-------------Title-------------------')
    print(driver.title)
    
    print('-------------Requests--------------------')
    
    for request in driver.requests:
        if request.response:
            print(request.response.status_code)
            print(request.url)
            #print(request.response.headers['Content-Type'])
    """       
            if request.response.status_code == 302:
                print(request.response.headers)
    """
    
    print('-------------Cookies--------------------')
    cookies = driver.get_cookies()
    for cookie in cookies:
        #print(cookie)
        print(cookie['name'])
        print(cookie['value'])
    print('-------------------------------------------------------------')
    print('--------------------------Cookie syncing---------------------')
    print('-------------------------------------------------------------')
    for request in driver.requests:
        if request.response:
            for cookie in cookies:
                params = parse_qs(urlparse(request.url).query)

                
                for p in params:
                    value = parse_qs(urlparse(request.url).query)[p][0]
                    
                    #case 4:

                    if(value in cookie['value'] and re.search("^GA.*\..*\.*\..*", cookie['value']) and re.search(".*\..*",value) and len(value)>=ID_MIN_LENGTH and len(cookie['value'])>=ID_MIN_LENGTH):
                        print("#case 4")
                        print("Cookie name ",cookie['name']," with value: ",cookie['value'])
                        print(" is found in Request url:",request.url)
                        print(" In param ",p, "With value", value)
                        
                    #case 1:
                    elif(value == cookie['value'] and len(value)>=ID_MIN_LENGTH and len(cookie['value'])>=ID_MIN_LENGTH):
                        print("#case 1")
                        print("Cookie name ",cookie['name']," with value: ",cookie['value'])
                        print(" is found in Request url:",request.url)
                        print(" In param ",p, "With value", value)

                    #case 2:

                    elif(cookie['value'] in value and len(value)>=ID_MIN_LENGTH and len(cookie['value'])>=ID_MIN_LENGTH):
                        print("#case 2")
                        print("Cookie name ",cookie['name']," with value: ",cookie['value'])
                        print(" is found in Request url:",request.url)
                        print(" In param ",p, "With value", value)

                    #case 3:

                    elif(value in cookie['value'] and len(value)>=ID_MIN_LENGTH and len(cookie['value'])>=ID_MIN_LENGTH):
                        print("#case 3")
                        print("Cookie name ",cookie['name']," with value: ",cookie['value'])
                        print(" is found in Request url:",request.url)
                        print(" In param ",p, "With value", value)

                    
                    

                    #case 5:

                    #case 6:

#driver.quit()