#alert('Hello!'); выводит высплывашку с текстом Hello!
from selenium import webdriver
browser = webdriver.Chrome()

alert = browser.switch_to.alert     #переключение на окно alert'a
alert.accept()                      #принятие

alert = browser.switch_to.alert     #переключение на окно alert'a
alert_text = alert.text             #получение текста окна alert'a

confirm = browser.switch_to.alert   #переключение на окно confirm'a
confirm.accept()                    #принятие
confirm.dismiss()                   #отказ

prompt = browser.switch_to.alert    #переключение на окно promt
prompt.send_keys("My answer")       #ввод текста
prompt.accept()                     #принятие
prompt.dismiss()                    #отказ