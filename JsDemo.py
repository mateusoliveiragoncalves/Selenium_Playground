# Js DOM can access every element on the page

# How to acess DOM from Selenium

from selenium import webdriver
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