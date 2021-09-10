from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

word = "Mateus"

driver.find_element_by_css_selector("#name").send_keys(word)

driver.find_element_by_css_selector("#alertbtn").click()

#Changin to alert mode and visualizae th JS Alerts on the DOM
alerta = driver.switch_to.alert
alertText= alerta.text

assert word in alertText

alerta.accept()