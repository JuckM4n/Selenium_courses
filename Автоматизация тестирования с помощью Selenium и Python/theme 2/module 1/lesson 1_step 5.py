from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    #Open site in browser
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    
    #Calculations
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    #Write our answer in special field
    answer_text = browser.find_element(By.CSS_SELECTOR, "input#answer")
    answer_text.send_keys(calc(x))
    #Press I'm the robot
    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")    
    checkbox.click()
    
    #Press Robots rule
    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()
    
    #Press submit button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    #Waiting 5 seconds and close browser
    time.sleep(5)
    browser.quit()
    