from re import*

text = "  Это   строка    с     большим    количеством   пробелов."
sch = r" +"
ans = sub(sch, " ", text)
sch2 = r"(?:^ +| +$)"
ans = sub(sch2, "", ans)
print(ans)