count_str = 0
count_sl = 0
count_sim = 0
max_dlin = 0
with open("text2", "r", encoding="utf-8") as file:
    for s in file:
        s = s.strip()
        count_str += 1
        slova = s.split(' ')
        count_sl += len(slova)
        count_sim += (len(s))
        if len(s) > max_dlin:
            max_dlin = len(s)

print(count_str)
print(count_sl)
print(count_sim)
print(max_dlin)