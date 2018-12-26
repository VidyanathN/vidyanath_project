from selenium import webdriver
import os
import time

class Abc():
    def set1(self):
        driverLocation="D:\\Selenium\\chromedriver_win32\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"]=driverLocation
        driver=webdriver.Chrome(driverLocation)
        driver.get("http://www.fb.com")
        print("First test is completed")
        time.sleep(5)
        
        
c=Abc()
c.set1()
