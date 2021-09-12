from selenium import webdriver
import time
from termcolor import colored
from colored import fg, bg, attr

driver = webdriver.Chrome()

driver.implicitly_wait(1)

driver.get("https://the-internet.herokuapp.com/iframe")

iframe = driver.find_element_by_xpath("//iframe[@id='mce_0_ifr']")

driver.switch_to.frame(iframe)

driver.find_element_by_css_selector("#tinymce").clear()

driver.find_element_by_css_selector("#tinymce").send_keys("Testing the Frame selection with Selenium")

frameText = driver.find_element_by_css_selector("#tinymce").text

print(colored(f'{frameText}',"green"))

driver.switch_to.default_content()

driver.close()

