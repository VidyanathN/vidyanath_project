from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
"""for cross browser testing"""

class Abc():
    def set1(self):
        driverLocation="D:\\Selenium\\chromedriver_win32\\geckodriver.exe"
        driver=webdriver.Firefox(driverLocation)
        driver.get("http://www.fb.com")
        
        
        
        
        
        
c=Abc()
c.set1()
