#Для более детальных проверок в тесте нам может понадобиться узнать значение атрибута элемента. Атрибуты могут быть стандартными свойствами, которые понимает и использует браузер для отображения и вёрстки элементов или для хранения служебной информации, например, name, width, height, color и многие другие. Также атрибуты могут быть созданы разработчиками проекта для задания собственных стилей или правил.
<input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>

#Найдём этот элемент с помощью WebDriver:
people_radio = browser.find_element(By.ID, "peopleRule")

#Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"

#Мы можем написать проверку другим способом, сравнив строки:
assert people_checked == "true", "People radio is not selected by default"

#Если атрибута нет, то метод get_attribute вернёт значение None. Применим метод get_attribute ко второму radiobutton, и убедимся, что атрибут отсутствует.
robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None

#Так же мы можем проверять наличие атрибута disabled, который определяет, может ли пользователь взаимодействовать с элементом. Например, в предыдущем задании на странице с капчей для роботов JavaScript устанавливает атрибут disabled у кнопки Submit, когда истекает время, отведенное на решение задачи.

<button type="submit" class="btn btn-default" disabled>Submit</button>