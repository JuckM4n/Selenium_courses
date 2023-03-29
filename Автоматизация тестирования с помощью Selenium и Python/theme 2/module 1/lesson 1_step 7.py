from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

#Open site in browser
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
    
#Calculations
x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
#Write our answer in special field
answer_text = browser.find_element(By.CSS_SELECTOR, "input#answer")
answer_text.send_keys(calc(x))
#Press I'm the robot
checkbox = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")    
checkbox.click()
    
#Press Robots rule
radio = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
radio.click()
    
#Press submit butto
button = browser.find_element(By.CSS_SELECTOR, "button.btn")

button.click()