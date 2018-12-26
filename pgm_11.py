from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
"""cross browser testing"""

class Abc():
    def set1(self):
        driverLocation="D:\\Selenium\\chromedriver_win32\\chromedriver.exe"
        driver=webdriver.Chrome(driverLocation)
        driver.get("http://www.google.com")
        driver.refresh()
        time.sleep(5)
        driver.get("http://www.fb.com")
        time.sleep(5)
        driver.back()
        time.sleep(5)
        driver.get("http://www.gmail.com")
        time.sleep(5)
        driver.back()
        driver.quit()
        
        
        
        
c=Abc()
c.set1()
