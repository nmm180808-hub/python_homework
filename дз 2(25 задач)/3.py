from csv import*

summ = 0
kol = 0
maxx_score = -1
sl_gr = {}
with open("students.csv", 'r', encoding="UTF-8", newline='') as file:
    students = DictReader(file)
    for s in students:
        score = int(s['score'])
        name = s['name']
        group = int(s['group'])
        summ+=score
        kol+=1
        if score > maxx_score:
            maxx_score = score
            maxx_name = name
        if group not in sl_gr:
            sl_gr[group] = [score, 1]
        else:
            sl_gr[group][0] += score
            sl_gr[group][1] += 1

    for el in sl_gr.values():
        print(el[0]/el[1])
    print(maxx_score)
    print(summ/kol)



