from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
"""radio button click"""

def set1():
    c="D:\\Selenium\\chromedriver_win32\\chromedriver.exe"
    driver=webdriver.Chrome(c)
    driver.get("https://learn.letskodeit.com")
    cookie={'fruit':'mango','chocalate':'milk'}
    driver.add_cookie(cookie)
    print(driver.get_cookies())
    
        

set1()
