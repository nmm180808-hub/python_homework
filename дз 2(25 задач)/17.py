summ = 0
maxx = -2e9
minn = 2e9
count = 0
average = 0
with open("17test.txt", "r", encoding="UTF-8") as file:
    for s in file:
        number = int(s)
        summ+=number
        if number > maxx:
            maxx = number
        if number < minn:
            minn = number
        count+=1

if count == 0:
    print("Файл пуст")
else:
    average = summ / count

    print("Сумма:", summ)
    print("Минимум:", minn)
    print("Максимум:", maxx)
    print("Количество:", count)
    print("Среднее:", average)

