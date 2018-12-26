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
        driver.get("http://www.fb.com")
        time.sleep(5)
        driver.find_element_by_name("email").send_keys("vidyanathnalla565@gmail.com")
        driver.find_element_by_name("pass").send_keys("nallavidyanath@12345")
        driver.find_element_by_tag_name('html').send_keys(Keys.END)
        time.sleep(5)
        driver.find_element_by_tag_name('html').send_keys(Keys.HOME)
        time.sleep(5)
        
        
c=Abc()
c.set1()
