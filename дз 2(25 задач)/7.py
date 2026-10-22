from pathlib import Path

path = Path(input())
suf = input()
#C:\Users\Acer\Documents\Университет\Лабораторные\лаб 1
#.c
print("*"+"ghbdtn")
if path.is_dir():
    for i in path.rglob("*"+suf):
        if i.is_file():
            print("Путь:", i)
            print("Размер:", i.stat().st_size)
else:
    print("Ошибка: каталог не существует")
