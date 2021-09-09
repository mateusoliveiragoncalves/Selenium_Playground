from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(f"The number of checkboxes on this page is {(len(checkboxes))}.")

for checkbox in checkboxes:
    checkbox.click()
    #validating the selection
    assert checkbox.is_selected()

time.sleep(3)

for checkbox in checkboxes:
    checkbox.click()
    #validating the selection
    assert checkbox.is_selected() is False
