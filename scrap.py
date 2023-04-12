import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user = "rhudson"
pwd = "r20000305."

DRIVER_PATH = 'C:/Users/Administrator/Downloads/chromedriver_win32'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://app.anonaddy.com/login")

element = driver.find_element(By.ID, "username")
element.send_keys(user)
element = driver.find_element(By.ID, "password")
element.send_keys(pwd)

submit = driver.find_element(By.TAG_NAME, "button").click()

driver.implicitly_wait(10)

driver.get("https://app.anonaddy.com/")

# Find all the <div> elements on the page
alias_rows = driver.find_elements(By.TAG_NAME, "tr")

# Loop through each <div> element and print its contents
alias_data = []

for row in alias_rows:
    alias_dict = {}
    cells = row.find_elements(By.TAG_NAME, "td")
    if cells != []:
        spans = cells[0].find_elements(By.TAG_NAME, "span")
        if spans != []:
            alias_dict["Alias"] = spans[2].text
        alias_dict["Forwarded"] = cells[1].text
        alias_dict["Created"] = cells[3].text
        btn = cells[6].find_element(By.TAG_NAME, "button")
        alias_dict["Active"] = btn.get_attribute("aria-checked")
    alias_data.append(alias_dict)

# Print the scraped data
with open("data.json", "w") as outfile:
    json.dump(alias_data, outfile)
driver.close()