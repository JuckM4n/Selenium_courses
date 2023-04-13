from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
class TestAbs(unittest.TestCase):
    def test_abs1(self): 
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        first = browser.find_element(By.CLASS_NAME, "form-control.first")
        first.send_keys("Nikita")
        second = browser.find_element(By.CLASS_NAME, "form-control.second")
        second.send_keys("Morozov")
        email = browser.find_element(By.CLASS_NAME, "form-control.third")
        email.send_keys("nik_morozov0@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
   
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        
        self.assertEqual(welcome_text, welcome_text_elt, "Congratulations! You have successfully registered!")
    
    def test_abs2(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
   
        first = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        first.send_keys("Nikita")
        second = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        second.send_keys("Morozov")
        email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        email.send_keys("nik_morozov0@mail.ru")
    
        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1").text
    
        self.assertEqual ("Congratulations! You have successfully registered!") == welcome_text_elt
    
if __name__ == "__main__":
    unittest.main()
    