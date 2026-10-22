from re import *

text = "Контакты: alice@example.com bob@test.org alice@example.com admin@company.ru"
lst = findall(r'[a-zA-Z0-9_%+-]+@[a-z]+\.[a-z]+', text)
print(set(lst))
