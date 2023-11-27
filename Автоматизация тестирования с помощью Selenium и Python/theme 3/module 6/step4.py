import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import array
import time
import math

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
class TestAuth():
    def test_auth(self, browser):
        link = "https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        time.sleep(2)
        signin = WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#ember33"))  
        )
        signin.click()
        email = WebDriverWait(browser, 20).until(
           EC.visibility_of_element_located((By.CSS_SELECTOR, "#id_login_email"))  
        )
        email.send_keys("nik_morozov0@mail.ru")
        password = WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located((By.ID, "id_login_password"))
        )
        password.send_keys("nirvana89")
        submit = WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.sign-form__btn"))
        )
        submit.click()