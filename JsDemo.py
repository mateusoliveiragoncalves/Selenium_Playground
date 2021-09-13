# Js DOM can access every element on the page

# How to acess DOM from Selenium

from selenium import webdriver
from selenium.webdriver import chrome
from termcolor import colored

driver = webdriver.Chrome()

driver.implicitly_wait(2)

driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element_by_name("name").send_keys("Mateus")

#You should get atributte value to return your text
print(colored(driver.find_element_by_name("name").get_attribute("value"),"green"))

#Executing JS inside selenium/Python with execute_script functions

#To find elements with JS you have to go to Conosole and type document.GETYOURJSSCRIPT

print(colored(f'This print is using only JS to get the element:\n',"red"),
      colored(driver.execute_script('return document.getElementsByName("name")[0].value',"yellow")))

shop_link = driver.find_element_by_link_text("Shop")

print(colored(shop_link.text,"green", attrs=['reverse', 'blink']))

#Using arguments to click with JS selectors
driver.execute_script("arguments[0].click();",shop_link)

# Script so scroll down to bottom and footer
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")