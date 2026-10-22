from re import*

s = "Полезные сайты: https://python.org, http://example.com/page,https://example.com/docs/index.html и ftp://files.example.com/data."

sch = r"(?:https|http)://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9._/-]*[a-zA-Z0-9_-])?"
lst = findall(sch, s)
print(lst)