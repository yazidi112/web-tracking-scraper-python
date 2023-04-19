from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import re
import base64
import json
from db import * 
from cookieManager import *
from paramsManager import *
from result import *

class Scraper:
    @staticmethod
    def run(data_url,min,max,ID_MIN_LENGTH):
        data = ['aljazeera.net']
        #data = ['localhost:9000']

        if(input("You want to load data from url ? [Y¦n]: ") != "n"):
            f = open(data_url)
            data = json.load(f)
            f.close()

        if(input("You want to clear database? [Y¦n]: ") != "n"):
            Site.clear()
            Request.clear()

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument('ignore-certificate-errors')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome("/usr/bin/chromedriver",chrome_options=chrome_options)
        #driver = webdriver.Firefox()
        
        for index,site in enumerate(data[min:max]):
            site = 'http://'+site
            print("________________________________________________________")
            print(index+1,": ",site)
            driver.get(site)
            print('-------------Title-------------------')
            print(driver.title)
            
            print('-------------Requests: 302 status code----------------')
            
            for request in driver.requests:
                if request.response:
                    location = request.response.headers['Location']
                    status = request.response.status_code
                    method = request.method
                    typ = request.response.headers["Content-Type"]
                    url = request.url
                    
                    if status == 302:
                        
                        cookies  = CookieManager.getCookies(request)
                        params = ParamsManager.getParams(location)

                        #print("REQUEST: ",request.headers)
                        #print("RESPONSE: ",request.response.headers)
                        print("LOCATION: ",location)                        
                        print("COOKIES: ",cookies)
                        
                        for cookie in cookies:
                            for param_name,param_value in params:
                                sharing_technique = "NONE"
                                #case 4:
                                if(param_value in cookie['value'] and re.search("^GA.*\..*\.*\..*", cookie['value']) and re.search(".*\..*",param_value) and len(param_value)>=ID_MIN_LENGTH and len(cookie['value'])>=ID_MIN_LENGTH):
                                    sharing_technique = "GAS"                                    

                                #case 1:
                                elif(param_value == cookie['value'] and len(param_value)>=ID_MIN_LENGTH and len(cookie['value'])>=ID_MIN_LENGTH):
                                    sharing_technique = "DS"
                                    
                                #case 2:
                                elif(cookie['value'] in param_value and len(param_value)>=ID_MIN_LENGTH and len(cookie['value'])>=ID_MIN_LENGTH):
                                    sharing_technique = "PP"
                                    
                                #case 3:
                                elif(param_value in cookie['value'] and len(param_value)>=ID_MIN_LENGTH and len(cookie['value'])>=ID_MIN_LENGTH):
                                    sharing_technique = "PC"
                                    
                                #case 5:
                                elif(param_value == base64.b64encode(cookie['value'].encode("utf-8")).decode("utf-8")):
                                    sharing_technique = "B64S"
                                
                                if(sharing_technique!="NONE"):
                                    print("Sharing technique: ",sharing_technique)
                                    print("In Request url:",location)
                                    print("Cookie name ",cookie["name"]," with value: ",cookie['value'])
                                    print(" is found matched with param ",param_name, "Which its value", param_value)
                                    Request.insert(site,url,typ,method,status,location,sharing_technique)
            
        Result.show()
            