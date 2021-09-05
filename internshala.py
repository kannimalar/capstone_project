from selenium import webdriver
from selenium import *
from time import sleep
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('headless')
driver = webdriver.Chrome(options=options,executable_path="F:\Engg Tools Lab\chromedriver.exe")
driver.get("https://internshala.com/fresher-jobs") 

close = driver.find_element_by_id("close_popup")
close.click()

def func(href_val):
    for link in href_val:
        driver.get(link) 
        desc = driver.find_element_by_xpath('//div[@class="text-container"]')
        print(desc.text)
    
    
def answer():
    href_val=[]
    containers = driver.find_elements_by_xpath('//div[@class="container-fluid individual_internship visibilityTrackerItem "]')
    
    for items in containers:
        Post_name = items.find_element_by_xpath('.//div[@class="heading_4_5 profile"]')
        print(Post_name.text)
    
        Company_name = items.find_element_by_xpath('.//div[@class="heading_6 company_name"]')
        print(Company_name.text)

        atag = items.find_element_by_xpath('.//a[@class="view_detail_button"]')
        href_val.append(atag.get_attribute('href'))
   
    func(href_val)
answer()

driver.quit()
