from datetime import datetime
import time

from selenium import webdriver

driver = webdriver.Chrome()

print("What country do you want to travel?")

choice = "ind"

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").send_keys(choice)

time.sleep(2)

countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")

for country in countries:
    if country.text == "India":
        country.click()
        break

assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"

driver.close()