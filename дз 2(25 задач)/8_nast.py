from pathlib import Path

def read_file(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print("Файл не найден")
    except PermissionError:
        print("Нет прав на чтение файла")
    except IsADirectoryError:
        print("Указан каталог, а не файл")
    except OSError:
        print("Ошибка при чтении файла")
    return None

path = Path(r"C:\Users\Acer\Documents\план презентаци.txt")
text = read_file(path)
if text is not None:
    print(text)
