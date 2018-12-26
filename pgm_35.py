from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os
import time
"""Handlin the alert in selenium python"""

def set1():
    c="D:\\Selenium\\chromedriver_win32\\chromedriver.exe"
    driver=webdriver.Chrome(c)
    driver.get("https://learn.letskodeit.com/p/practice")
    time.sleep(6)
    driver.execute_script("window.alert('This is alert')")
    time.sleep(6)
    alert=driver.switch_to_alert()
    alert.dismiss()
    time.sleep(6)

set1()
