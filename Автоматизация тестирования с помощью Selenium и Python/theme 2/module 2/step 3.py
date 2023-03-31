from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/selects2.html")

x_element = browser.find_element(By.ID, "num1")
y_element = browser.find_element(By.ID, "num2")
a = x_element.text
b = y_element.text
x = int(a)
y = int(b)

def sum(x, y):
    return str (x + y)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(sum(x, y)) # ищем value в списке

button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(5)