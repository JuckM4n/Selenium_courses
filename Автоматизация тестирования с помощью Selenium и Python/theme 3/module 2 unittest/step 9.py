#Жетские правила провреки на полное совпадение - in или find
s = 'My Name is Julia'

if 'Name' in s:                                         #возвращает просто True или False
    print('Substring found')

index = s.find('Name')                                  #find() возвращает индекс первого вхождения подстроки в строку и -1, если подстрока не найдена
if index != -1:
    print(f'Substring found at index {index}')
    
#Обычно в автотестах достаточно использовать in, потому что это более читабельный вариант.

#Например, для проверки того, что в текущем url содержится строка login: 
assert "login" in browser.current_url, # сообщение об ошибке
