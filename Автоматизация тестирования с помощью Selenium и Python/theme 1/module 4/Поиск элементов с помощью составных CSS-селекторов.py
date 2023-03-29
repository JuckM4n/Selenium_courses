#Поиск по id
"#bullet"

#Поиск по tag
"h1"

#Поиск по значению атрибута
"[id="bullet"]"

#Поиск по name
"[name="bullet-cat"]"

#Поиск по class
"[class="jumbotron-heading"]" или ".jumbotron-heading"
#Если несколько классов, то либо пишем
"[class="lead text-muted"], так как порядок классов при этом важен то [class="text-muted lead"] — уже не найдет искомый элемент."
#либо
".lead .lead.text-muted или .text-muted.lead т.к. данный способ ищет простое вхождение класса в элемент. РЕГИСТР ВАЖЕН!"

#Использование потомков
"#post2 .title"

#Использование дочерних элементов
"#post2 > div.title"

#Использование порядкового номера дочернего элемента
"#posts > .item:nth-child(2) > .title"

#Использование нескольких классов
".title.second"

#Поиск по всему тексту
link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
link.click()

#Поиск по части текста
link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")
link.click()

:nth-child() - выбор "ребенка" в css