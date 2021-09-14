import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from termcolor import colored

# CHROME OPTIONS LIST --> https://peter.sh/experiments/chromium-command-line-switches/

#initiating the chromeoptions
chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

#headless argument --> executes on the backend not invoking the browser
# chrome_options.add_argument("headless")
# chrome_options.add_argument("--ignore-certificate-errors")

#passing the options to our driver with (options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(3)

driver.get('https://rahulshettyacademy.com/angularpractice/')

# 1 Step: Enter to the page and click in "Shop" button

driver.find_element_by_css_selector("a[href*='shop']").click()

# 2 Step: Find the elements who haves the same characteristics

products = driver.find_elements_by_xpath("//div[@class='card h-100']")

# 3 Step Iterate the element to found the producti that you want using for and if
for product in products:
    if product.find_element_by_xpath("div/h4/a").text == "Blackberry":
        print(colored(f'{product.find_element_by_xpath("div/h4/a").text} was found!',"green",attrs=['blink','bold']))
        # 4 Step Let's add this product to the cart:
        product.find_element_by_xpath("div[2]/button").click()

#5 - Click on the checkout Button:
driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

#6 - dELIVERY INFORMATIONS
driver.find_element_by_id("country").send_keys("Uni")

wait = WebDriverWait(driver,7)
country = "United States of America"
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,country)))
driver.find_element_by_link_text("United States of America").click()
print(colored(f'{country} was set as your address!', "blue", attrs=['blink', 'bold']))
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[type='submit']").click()

#7 - Asserting the Transaction success:
success_message = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
assert "Success!" in success_message
print(colored(f'{success_message} Mateus', "magenta", attrs=['blink', 'bold']))

# 8 - taking a screenshot of the last step
driver.get_screenshot_as_file("endtoend.png")

# Bye :D

print(colored("See you in another day!","yellow", attrs=['blink', 'bold']))