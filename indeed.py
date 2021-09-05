from selenium import webdriver
from selenium import *
from time import sleep
from selenium.webdriver.common.keys import Keys

from datetime import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ast import literal_eval
time=datetime.now()
import codecs

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('headless')
driver = webdriver.Chrome(options=options,executable_path="F:\Engg Tools Lab\chromedriver.exe")
driver.get("https://in.indeed.com/jobs?q=&l=India&sort=date") 

# close = driver.find_element_by_id("close_popup")
# close.click()

def func(href_val):
    for link in href_val:
        driver.get(link) 
        desc = driver.find_element_by_xpath('//div[@class="jobsearch-JobComponent-description icl-u-xs-mt--md"]')
        desc=desc.text
        # desc = desc.encode('utf-8')
        
        desc = desc.encode("unicode_escape")
        #codecs.decode(desc, 'unicode_escape')
        desc = str(desc)
        desc = desc.replace("\\\\","\\")
        desc = desc.replace("\\n"," ")
        desc = desc.replace("\\u20b"," ")
        desc = desc.replace("\\u2013"," ")
        print(desc)
    
    
def answer():
    href_val=[]
    containers = driver.find_elements_by_xpath('//div[@class="mosaic mosaic-provider-jobcards mosaic-provider-hydrated"]/a')
    
    for items in containers:
        # Post_name = items.find_element_by_xpath('.//div[@class="heading4 color-text-primary singleLineTitle tapItem-gutter"]/h2/span')
        # print(Post_name.text)
    
        Company_name = items.find_element_by_xpath('.//div[@class="heading6 company_location tapItem-gutter"]/pre/span')
        print(Company_name.text)

        href_val.append(items.get_attribute('href'))
        #print(items.get_attribute('href'))
   
    func(href_val)
answer()

driver.quit()
print(datetime.now()-time)
