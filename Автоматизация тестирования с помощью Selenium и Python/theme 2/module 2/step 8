from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

first_name = browser.find_element(By.NAME, "firstname").send_keys("Nikita")
last_name = browser.find_element(By.NAME, "lastname").send_keys("Morozov")
email = browser.find_element(By.NAME, "email").send_keys("juckm4n@gmail.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
imput_file = browser.find_element(By.ID, "file").send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(5)