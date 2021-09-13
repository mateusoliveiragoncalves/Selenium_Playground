from selenium import webdriver
from termcolor import colored

# CHROME OPTIONS LIST --> https://peter.sh/experiments/chromium-command-line-switches/


#initiating the chromeoptions
chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

#headless argument --> executes on the backend not invoking the browser
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

#passing the options to our driver with (options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(2)

driver.get('https://rahulshettyacademy.com/angularpractice/')

print(colored(driver.title,"green",attrs=['blink','bold']))