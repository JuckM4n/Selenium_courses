#для более точного описания того, что тестировалось в данном месте (в логе информация выводится более информативно)
assert abs(-42) == 42, "Should be absolute value of a number"

#важно давать его точно и актуально. Если вы проверяете наличие элемента, то обязательно пишите, что это за элемент по смыслу на странице
assert self.is_element_present('create_class_button', timeout=30), "No create class button"

#Если элемент встречается на нескольких страницах приложения, не лишним будет указать, где именно произошла ошибка: 
assert self.is_element_present('new_announcement_button', timeout=30), "No new announcement button on profile page"

#Если вы работаете с каким-то текстом (например, проверяете информационное сообщение, текущий url, ссылку, placeholder в input-элементе или любой другой текст)
#в сообщении об ошибке всегда лучше выводить оба значения: то, которое ожидалось, и то, которое получили по факту. Всё как в хорошем багрепорте: ожидаемый и фактический результат.


#Форматирование строк с помощью конкатенации
#В питоне такое можно провернуть с помощью конкатенации строк, например:
actual_result = "abrakadabra"
print("Wrong text, got " + actual_result + ", something wrong")

#Форматирование строк с помощью str.format
#Если вкратце, то python умеет подставлять пользовательские значения в строки с помощью функции .format(). Синтаксис выглядит примерно так:
"Let's count together: {}, then goes {}, and then {}".format("one", "two", "three")

#Форматирование строк с помощью f-strings
#Для использования возможностей f-strings нужно указывать символ f перед строкой в таком формате: f"ваша строка {my_var}".
#В фигурных скобках указывается имя переменной, значение которой надо подставить в строку, или выражение, результат исполнения которого также требуется подставить в вашу строку.
#Пример 1:
str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

#Итог выполнения выражений в интерпретаторе:
Let's count together: one, then goes two, and then three

#Пример 2:
actual_result = "abrakadabra"
f"Wrong text, got {actual_result}, something wrong"

#Итог выполнения выражений в интерпретаторе:
Wrong text, got abrakadabra, something wrong

#Пример 3:
f"{2+3}"
'5'

#Еще один важный момент: когда вы работаете с текстом элементов на странице или любым другим контентом, который может измениться, всегда записывайте его в отдельную переменную для сравнения. 
#неправильно:
assert self.catalog_link.text  == "Каталог", \
    f"Wrong language, got {self.catalog_link.text} instead of 'Каталог'" 
    
"Wrong language, got 'Каталог' instead of 'Каталог'" #результат выполнения такого теста сложно анализировать: 
    
#правильно:
catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
    f"Wrong language, got {catalog_text} instead of 'Каталог'"  