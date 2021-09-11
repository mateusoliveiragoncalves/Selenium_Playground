from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

cart = driver.find_element_by_css_selector("img[alt='Cart']")

cart.click()

proceed = driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]")

wait = WebDriverWait(driver,5)

wait.until(EC.presence_of_element_located((By.CLASS_NAME,"promoCode")))

proceed.click()

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_class_name("promoBtn").click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))

code_applied = driver.find_element_by_css_selector("span.promoInfo").text

print(code_applied)

assert code_applied == "Code applied ..!"

driver.close()




