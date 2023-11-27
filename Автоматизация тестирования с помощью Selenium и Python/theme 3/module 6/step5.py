from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from selenium import webdriver
import time
import math
import pytest

# для старта pytest -v -s 3_6_3_step_OWLS_OvO.py
# s, чтоб видеть print
# v, для того, чтобы запустить расширенный визуальный режим

uncorrected_results = []

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(55)
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(''.join(uncorrected_results))

@pytest.mark.parametrize('link_task', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_find_ufo(browser, link_task):
    link = f"https://stepik.org/lesson/{link_task}/step/1"
    browser.get(link)
    
    signin_button = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CLASS_NAME, "ember-view.navbar__auth")))
    signin_button.click()
    time.sleep(2)

    email = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, "#id_login_email")))
    email.send_keys("nik_morozov0@mail.ru")
    
    password = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.ID, "id_login_password")))
    password.send_keys("Nirvana89")
    
    submit = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CLASS_NAME, "sign-form__btn")))
    submit.click()
    time.sleep(2)
    
    answer_place = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]')))
    answer_place.send_keys(str(math.log(int(time.time()))))

    submit_button = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[class="submit-submission"]')))
    submit_button.click()

    option_text = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[class="smart-hints__hint"]'))).text

    if option_text != "Correct!":
        uncorrected_results.append(option_text)

    assert "Correct!" == option_text, f'Error: {option_text}'