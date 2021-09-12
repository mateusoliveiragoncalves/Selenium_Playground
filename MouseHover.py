from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from termcolor import colored
from colored import fg, bg, attr

driver = webdriver.Chrome()

driver.implicitly_wait(1)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#Importing Actyion Chains to hover
action = ActionChains(driver)

hover_button = driver.find_element_by_id('mousehover')

action.move_to_element(hover_button).perform()

print(hover_button.text)

childMenu = driver.find_element_by_link_text("Top")

action.move_to_element(childMenu).click().perform()



