from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radioButtons = driver.find_elements_by_xpath("//input[@name='radioButton']")

print(f"The number of checkboxes on this page is {(len(radioButtons))}.")

for button in radioButtons:
    button.click()
    time.sleep(1.5)
    #validating the selection
    assert button.is_selected()

time.sleep(2)

# chose only the option2
for button in radioButtons:
    if button.get_attribute('value') == "radiobutton3":
        button.click()
        #validating the selection
        assert button.is_selected()