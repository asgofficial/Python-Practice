import numpy as np

marks = np.array([
    [45, 85, 70],   # Student 0
    [60, 75, 80],   # Student 1
    [40, 90, 65],   # Student 2
    [95, 55, 88],   # Student 3
    [50, 82, 76]    # Student 4
])

print("Marks Array:")
print(marks)

print("\n1. Maximum marks:", np.max(marks))
print("2. Minimum marks:", np.min(marks))
print("3. Average marks:", np.mean(marks))
print("4. Maximum marks subjectwise:", np.max(marks, axis=0))
print("5. Average marks subjectwise:", np.mean(marks, axis=0))

student_id = np.argmax(marks[:, 0])
print("6. Student ID with maximum marks in Subject 1:", student_id)

marks[marks[:, 0] < 50, 0] += 10
print("7. Array after adding 10 marks:")
print(marks)

count = np.sum(marks[:, 1] > 80)
print("8. Students scoring more than 80 in Subject 2:", count)
print("9. Minimum marks of Student 2:", np.min(marks[2]))
print("10. Maximum marks of Student 4:", np.max(marks[4]))