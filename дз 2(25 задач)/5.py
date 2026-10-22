from json import *

with open("5num.json", "r", encoding="utf-8") as file:
    students = load(file)
    if len(students) != 0:
        best_student = max(students, key=lambda student :student ["score"])

    for student in students:
        if student["score"] >= 60:
            student["passed"] = True
        else:
            student["passed"] = False

print("Студент с максимальным баллом:", best_student["name"])
print("Его балл:", best_student["score"])

with open("5ans.json", "w", encoding="utf-8") as file:
    dump(students, file, ensure_ascii=False, indent=4)



