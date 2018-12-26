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
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.find_element_by_xpath("//input[@id='bmwradio']").send_keys(Keys.CONTROL+'a')
        time.sleep(5)
        
        
c=Abc()
c.set1()
