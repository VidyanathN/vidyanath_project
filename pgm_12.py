from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
"""cross browser testing"""

class Abc():
    def set1(self):
        driverLocation="D:\\Selenium\\python\\geckodriver-v0.23.0-win64\\geckodriver.exe"
        driver=webdriver.Firefox(driverLocation)
        driver.get("http://www.gmail.com")

        
        
        
        
c=Abc()
c.set1()
