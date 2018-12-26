from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
"""for cross browser testing"""

class Abc():
    def set1(self):
        driverLocation="D:\Selenium\chromedriver_win32\chromedriver.exe"
        driver=webdriver.Chrome(driverLocation)
        driver.get("http://www.fb.com")
        driver.get("http://www.gmail.com")
        driver.back()
        time.sleep(5)
        driver.forward()
        
        
        
        
        
c=Abc()
c.set1()
