import time

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")

time.sleep(2)

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

cart = driver.find_element_by_css_selector("img[alt='Cart']")

cart.click()

proceed = driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]")

proceed.click()




