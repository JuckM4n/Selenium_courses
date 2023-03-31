from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

#Open site in browser
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")
    
#Calculations
x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser.execute_script("window.scrollBy(0, 100);")
    
#Write our answer in special field
answer_text = browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(calc(x))

#Press I'm the robot
checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()    
  
#Press Robots rule
radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()

#Press submit button
button = browser.find_element(By.TAG_NAME, "button")
button.click()
time.sleep(5)