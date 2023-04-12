from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)
button = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.ID, "book"))
)

#browser.execute_script("return arguments[0].scrollIntoView(true);", button)

button.click()
x = browser.find_element(By.ID, "input_value").text
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

answer_text = browser.find_element(By.ID, "answer").send_keys(calc(x))

submit = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.ID, "solve"))
)
browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
submit.click()
time.sleep(10)