from re import *

s = "Звони +7 999 123-45-67 или 8 (999) 123-45-67. Номер 12345 не подходит."

sch = r"(?:\+7|8)\s+(?:\(\d{3}\)|\d{3})\s+\d{3}-\d{2}-\d{2}"

lst = findall(sch, s)

for number in lst:
    print(number)