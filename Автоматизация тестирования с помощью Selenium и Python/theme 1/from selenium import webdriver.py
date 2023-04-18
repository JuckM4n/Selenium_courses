import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.youtube.com/")
print("Application title is ", driver.title)
print("Application url is ", driver.current_url)
time.sleep(5)
driver.quit()