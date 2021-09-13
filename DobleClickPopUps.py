from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from termcolor import colored
from colored import fg, bg, attr

driver = webdriver.Chrome()

driver.implicitly_wait(1)

driver.get("https://www.chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action = ActionChains(driver)

double_click_button = driver.find_element_by_id("double-click")

action.double_click(double_click_button).click().perform()

alert = driver.switch_to.alert

assert alert.text == "You double clicked me!!!, You got to be kidding me"

print(colored(alert.text,"blue"))

alert.accept()






