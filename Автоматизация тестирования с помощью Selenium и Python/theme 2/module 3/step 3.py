from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

alert_btn = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(1)
alert = browser.switch_to.alert     #переключение на окно alert'a
alert.accept()

x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

answer_text = browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(calc(x))

submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()