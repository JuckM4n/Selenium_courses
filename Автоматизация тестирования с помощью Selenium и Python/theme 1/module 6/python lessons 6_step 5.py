from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"
form = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.LINK_TEXT, form)
    button.click()
    
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Nikita")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Morozov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Moscow")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()
    