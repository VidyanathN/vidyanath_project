from selenium import webdriver
import os
import time

class Abc():
    def set1(self):
        driverLocation="D:\\Selenium\\chromedriver_win32\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"]=driverLocation
        driver=webdriver.Chrome(driverLocation)
        driver.get("http://www.fb.com")
        dri=driver.find_element_by_css_selector("//input#email")
        dri.send_keys("vidyanathnalla565@gmail.com")
        dri=driver.find_element_by_css_selector("#pass")
        dri.send_keys("nallavidyanath@12345")
        dri=driver.find_element_by_css_selector("#u_0_2")
        dri.click()
        time.sleep(10)
        
        
c=Abc()
c.set1()
