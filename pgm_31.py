from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os
import time
"""radio button click"""

def set1():
    c="D:\\Selenium\\chromedriver_win32\\chromedriver.exe"
    driver=webdriver.Chrome(c)
    driver.get("https://learn.letskodeit.com/p/practice")
    ele=driver.find_element_by_xpath("//input[@id='bmwradio']")
    act=ActionChains(driver)
    act.context_click(ele).perform()
    time.sleep(5)
        

set1()
