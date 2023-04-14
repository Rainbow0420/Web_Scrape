# Form Submit Sample

# import json
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# user = "rhudson"
# pwd = "r20000305."

# DRIVER_PATH = 'C:/Users/Administrator/Downloads/chromedriver_win32'

# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver.get("https://profile.w3schools.com/log-in")

# element = driver.find_element(By.NAME, "email")
# element.send_keys(user)
# element = driver.find_element(By.NAME, "current-password")
# element.send_keys(pwd)

# submit = driver.find_element(By.TAG_NAME, "button").click()

# driver.implicitly_wait(10)

# driver.get("https://profile.w3schools.com/")

# Sample

import mechanize
import requests
brwsr = mechanize.Browser()
brwsr.open('https://profile.w3schools.com/log-in')
brwsr.select_form(nr = 0)
brwsr['email'] = 'openwindower@gmail.com'
brwsr['password'] = 'Qwe&*(789@'
response = brwsr.submit()
brwsr.submit()