def parse_number(value):
    if '.' in value:
        return float(value)
    return int(value)

value = input()
try:
    number = parse_number(value)
    print("Полученное число", number)
except ValueError:
    print("Ошибка: введено некорректное число")