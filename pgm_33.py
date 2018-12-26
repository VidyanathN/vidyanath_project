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
    time.sleep(6)
    ele=driver.find_element_by_xpath("//button[@id='mousehover']")
    act=ActionChains(driver)
    act.move_to_element(ele).perform()
    time.sleep(5)
        

set1()
