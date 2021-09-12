from selenium import webdriver
import time
from termcolor import colored
from colored import fg, bg, attr

driver = webdriver.Chrome()

driver.implicitly_wait(1)

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()

child_window = driver.window_handles[1]

driver.switch_to.window(child_window)

print(colored(driver.find_element_by_tag_name("h3").text,"green"))

main_window = driver.window_handles[0]

driver.switch_to.window(main_window)

print(colored(driver.find_element_by_tag_name("h3").text,"red"))