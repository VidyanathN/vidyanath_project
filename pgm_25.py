from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
"""radio button click"""

def set1():
    c="D:\\Selenium\\chromedriver_win32\\chromedriver.exe"
    driver=webdriver.Chrome(c)
    driver.get("https://learn.letskodeit.com/p/practice")
    time.sleep(5)
    driver.set_window_size(1024,768)
    time.sleep(5)
    print (driver.get_window_size())
    time.sleep(5)
    driver.close()
        

set1()
