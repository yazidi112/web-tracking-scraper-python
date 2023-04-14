from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
from urllib.parse import parse_qs
import re
import base64
from db import *

class Scraper:
    @staticmethod
    def run(data,min,max,ID_MIN_LENGTH):
        Site.clear()
        Request.clear()
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument('ignore-certificate-errors')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome("/usr/bin/chromedriver",chrome_options=chrome_options)
        #driver = webdriver.Firefox()
        cases = [0,0,0,0,0,0]
        for index,site in enumerate(data[min:max]):
            site = 'https://'+site
            print(index,": ",site)
            cases = [0,0,0,0,0,0]
            driver.get(site)
            print('-------------Title-------------------')
            print(driver.title)
            print('-------------Cookies--------------------')
            cookies = driver.get_cookies()
            
            for request in driver.requests:
                if request.response:
                    if request.response.status_code == 302:
                        cookie = request.response.headers['Set-Cookie']                
                        if(cookie is not None):
                            cookie_value = cookie.split(";",1)[0].split("=",1)[1]
                            cookie_name = cookie.split(";",1)[0].split("=",1)[0]
                            cookies.append({"name":cookie_name,"value":cookie_value})

            for cookie in cookies:
                print(cookie)
            
            print('-------------Requests--------------------')
            
            for request in driver.requests:
                if request.response:
                    location = request.response.headers['Location']
                    status = request.response.status_code
                    method = request.method
                    typ = request.response.headers["Content-Type"]
                    url = request.url
                    print(request.response.status_code)
                    print(request.url)
                    print(request.response)
                    
                    if status == 302:
                        
                        print('-------------------------------------------------------------')
                        print('------------------------- Start Cookie syncing --------------------')
                        print('-------------------------------------------------------------')
                        
                        print("Location: ",location)
                        for cookie in cookies:
                            cookie_value = cookie['value']
                            cookie_name = cookie["name"]
                            print("Cookie ",cookie_name," :",cookie_value)
                            params = parse_qs(urlparse(location).query)
                            for param in params:
                                param_value = parse_qs(urlparse(location).query)[param][0]
                                
                                #case 4:
                                
                                if(param_value in cookie_value and re.search("^GA.*\..*\.*\..*", cookie_value) and re.search(".*\..*",param_value) and len(param_value)>=ID_MIN_LENGTH and len(cookie_value)>=ID_MIN_LENGTH):
                                    print("#case 4: GA sharing")
                                    print("In Request url:",location)
                                    print("Cookie name ",cookie_name," with value: ",cookie_value)
                                    print(" is found matched with param ",param, "Which its value", param_value)
                                    cases[3]=cases[3]+1
                                    sharing_technique = "GAS"
                                    Request.insert(site,url,typ,method,status,location,sharing_technique)

                                #case 1:
                                elif(param_value == cookie_value and len(param_value)>=ID_MIN_LENGTH and len(cookie_value)>=ID_MIN_LENGTH):
                                    print("#case 1: direct sharing")
                                    print("In Request url:",location)
                                    print("Cookie name ",cookie_name," with value: ",cookie_value)
                                    print(" is found matched with param ",param, "Which its value", param_value)
                                    cases[0]=cases[0]+1
                                    sharing_technique = "DS"
                                    Request.insert(site,url,typ,method,status,location,sharing_technique)

                                #case 2:

                                elif(cookie_value in param_value and len(param_value)>=ID_MIN_LENGTH and len(cookie_value)>=ID_MIN_LENGTH):
                                    print("#case 2: Id as part of param")
                                    print("In Request url:",location)
                                    print("Cookie name ",cookie_name," with value: ",cookie_value)
                                    print(" is found matched with param ",param, "Which its value", param_value)
                                    cases[1]=cases[1]+1
                                    sharing_technique = "PP"
                                    Request.insert(site,url,typ,method,status,location,sharing_technique)

                                #case 3:

                                elif(param_value in cookie_value and len(param_value)>=ID_MIN_LENGTH and len(cookie_value)>=ID_MIN_LENGTH):
                                    print("#case 3: Id as part of Cookie")
                                    print("In Request url:",location)
                                    print("Cookie name ",cookie_name," with value: ",cookie_value)
                                    print(" is found matched with param ",param, "Which its value", param_value)
                                    cases[2]=cases[2]+1
                                    sharing_technique = "PC"
                                    Request.insert(site,url,typ,method,status,location,sharing_technique)

                                #case 5:

                                elif(param_value == base64.b64encode(cookie_value.encode("utf-8")).decode("utf-8")):
                                    print("#case 5: base64 sharing")
                                    print("In Request url:",location)
                                    print("Cookie name ",cookie_name," with value: ",cookie_value)
                                    print(" is found matched with param ",param, "Which its value", param_value)
                                    cases[4]=cases[4]+1
                                    sharing_technique = "B64S"
                                    Request.insert(site,url,typ,method,status,location,sharing_technique)

                        print('-------------------------------------------------------------')
                        print('------------------------- End Cookie syncing --------------------')
                        print('-------------------------------------------------------------')
            print('-------------------------------------------------------------')
            print('------------------------- Results --------------------')
            print('-------------------------------------------------------------')
            print(cases)
            Site.insert(site,cases[0],cases[1],cases[2],cases[3],cases[4])
            #driver.quit()