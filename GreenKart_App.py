'''
This app will test the cicle of selection products to the carts, apply discounts and assert if its applied and
the numbers are good.

It's a feature for used in the e-commerce websites usually to check their functions and ensure.
'''

from selenium import webdriver
import time

from termcolor import colored

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")

time.sleep(2)

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

products = []

products_final = []

for button in buttons:
    products.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

print(colored("products_list =>",'blue'),colored(f'{products}','yellow'))

cart = driver.find_element_by_css_selector("img[alt='Cart']")

cart.click()

proceed = driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]")

proceed.click()

time.sleep(1)

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_class_name("promoBtn").click()

products_purchased = driver.find_elements_by_class_name("product-name")

for product in products_purchased:
    products_final.append(product.text)

assert products_final == products

time.sleep(1)

code_applied = driver.find_element_by_css_selector("span.promoInfo").text

print(code_applied)

assert code_applied == "Code applied ..!"

total_amount = float(driver.find_element_by_class_name("totAmt").text)
discount_amount = float(driver.find_element_by_class_name("discountAmt").text)

if code_applied == "Code applied ..!":
    assert total_amount > discount_amount

sum_amount = 0

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")

for amount in amounts:
    sum_amount += int(amount.text)

assert sum_amount == total_amount

print(colored("Total_Cost = ",'blue'),colored(f'{sum_amount}','red'))

print(colored("Discount = ",'blue'),colored(f'{(sum_amount - discount_amount):.2f}','green'))

print(colored("Net Value = ",'blue'),colored(f'{(discount_amount):.2f}','magenta'))

print(colored("Everything Working Well", 'green'))


driver.close()




