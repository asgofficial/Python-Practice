students = [
    ("Rohul", 85),
    ("Alex", 72),
    ("Prisha", 95),
    ("Dimple", 68),
    ("Sanchita", 88),
    ("Ayush", 76),
    ("Mousani", 91),
    ("Karan", 63),
    ("Anish", 82),
    ("Arav", 78)
]

max_marks = max(student[1] for student in students)
min_marks = min(student[1] for student in students)


max_stu = [student[0] for student in students if student[1] == max_marks]
min_stu = [student[0] for student in students if student[1] == min_marks]

print("Student(s) scoring maximum marks:", max_stu)
print("Maximum marks:", max_marks)

print("Student(s) scoring minimum marks:", min_stu)
print("Minimum marks:", min_marks)