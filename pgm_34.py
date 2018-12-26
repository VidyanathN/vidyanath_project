from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os
import time
"""zoom in webpage"""

def set1():
    c="D:\\Selenium\\chromedriver_win32\\chromedriver.exe"
    driver=webdriver.Chrome(c)
    driver.get("https://learn.letskodeit.com/p/practice")
    time.sleep(6)
    driver.execute_script("document.body.style_zoom='150%'")
    time.sleep(6)
        

set1()
