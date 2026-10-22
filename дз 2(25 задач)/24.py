from re import*
sch = r"PRD-[0-9]{5}"
ans = []
products = [
    "PRD-12345",
    "PRD-00123",
    "USR-12345",
    "PRD-987",
    "PRD-ABCDE",
    "PRD-54321"
]
for el in products:
    lst = findall(sch, el)
    if len(lst) != 0:
        ans.append(el)

print(ans)

