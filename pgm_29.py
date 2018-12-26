from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
"""radio button click"""

def set1():
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver=webdriver.chrome(chrome_options=ChromeOtions)
    driver.get("www.gmail.com")
    
set1()
