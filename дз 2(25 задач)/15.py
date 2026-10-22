from io import StringIO

def count_lines(stream):
    count = 0
    for i in stream:
        count+=1
    return count

with open("text.txt", encoding="utf-8") as f:
    print(count_lines(f))

print(count_lines(StringIO("first\nsecond\nthird")))   
print(count_lines(StringIO("")))
print(count_lines(StringIO("a\n")))
print(count_lines(StringIO("a\n\nb")))