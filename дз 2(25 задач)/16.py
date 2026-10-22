from re import*

s = "2026-09-23 10:15:32 INFO User 123 logged in 2026-09-23 10:16:01 ERROR User 456 authentication failed 2026-09-23 10:17:43 WARNING User 123 changed password"

sch_inf = r"INFO User ([0-9]+)"
sch_war = r"WARNING User ([0-9]+)"
sch_error = r"ERROR User ([0-9]+)"

lst_inf = findall(sch_inf, s)
lst_war = findall(sch_war, s)
lst_error = findall(sch_error, s)

print(f"INFO: {len(lst_inf)}")
print(f"WARNING: {len(lst_war)}")
print(f"ERROR: {len(lst_error)}")
print(f"USER ERROR: ")
for el in set(lst_error):
    print(el)
    print()