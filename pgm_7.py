from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
"""facebook login and logout"""

class Abc():
    def set1(self):
        driverLocation="D:\\Selenium\\chromedriver_win32\\chromedriver.exe"
        driver=webdriver.Chrome(driverLocation)
        driver.get("http://www.gmail.com")
        time.sleep(10)
        driver.find_element_by_name("identifier").send_keys("vidyanathnalla3@gmail.com")
        driver.find_element_by_link_text("Next").click()
        
        
        
c=Abc()
c.set1()
