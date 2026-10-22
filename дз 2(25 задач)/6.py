from pathlib import Path

path = Path(r"C:\Users\Acer\Documents\Университет\Лабораторные\лаб 1")
count_file = 0
count_pk = 0
lst_py = []
summ_size = 0
if path.is_dir():
    for i in path.iterdir():
        if i.is_file():
            count_file +=1
            summ_size+=i.stat().st_size
            if i.suffix == '.py':
                lst_py.append(i.name)

        elif i.is_dir():
            count_pk+=1

print("Количество файлов:", count_file)
print("Количество подкаталогов:", count_pk)
print("Файлы .py:", lst_py)
print("Суммарный размер файлов:", summ_size, "байт")
