#Давайте попробуем вызвать alert в браузере с помощью WebDriver. Пример сценария:

from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")

#Если внутри скрипта вам также понадобится использовать кавычки, а для выделения скрипта вы уже используете двойные кавычки, то в скрипте следует поставить одинарные:

browser.execute_script("document.title='Script executing';")
#Такой формат записи тоже будет работать:

browser.execute_script('document.title="Script executing";')

#Изменим сначала заголовок страницы, а затем вызовем alert:

browser.execute_script("document.title='Script executing';alert('Robots at work');")