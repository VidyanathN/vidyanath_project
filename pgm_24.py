from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
"""radio button click"""

def set1():
    c="D:\\Selenium\\chromedriver_win32\\chromedriver.exe"
    driver=webdriver.Chrome(c)
    driver.get("https://learn.letskodeit.com/p/practice")
    driver.find_element_by_xpath("//input[@id='bmwcheck']").click()
    time.sleep(5)  
        

set1()
