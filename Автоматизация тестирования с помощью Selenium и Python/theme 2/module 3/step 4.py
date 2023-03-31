from selenium import webdriver
browser = webdriver.Chrome()

#Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти. Это делается с помощью команды switch_to.window:
browser.switch_to.window(window_name)

new_window = browser.window_handles[1] #возвращаем вторую вкладку

first_window = browser.window_handles[0] #запоминаем имя текущей вкладки