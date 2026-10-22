maxx = -2e9
minn = 2e9
summ = 0
kol = 0
with open("numbers.txt", "r", encoding="utf-8") as file_in:
    for s in file_in:
        try:
            if int(s) > maxx:
                maxx = int(s)
            if int(s) < minn:
                minn = int(s)

            summ+=int(s)
            kol+=1
        except ValueError:
            pass



with open("result.txt", "w", encoding="utf-8") as file_out:
    file_out.write(str(minn) + '\n')
    file_out.write(str(maxx) + '\n')
    if kol > 0:
        file_out.write(str(summ/kol) + '\n')
    else:
        file_out.write("0" + '\n')
            