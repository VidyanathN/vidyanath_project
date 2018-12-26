from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
"""facebook login and logout"""

def set1():
    c="D:\\Selenium\\chromedriver_win32\\geckodriver.exe"
    driver=webdriver.Firefox(c)
    driver.get("http://www.fb.com")
        
        

set1()
