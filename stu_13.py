# Creating Student dictionary
student = {
    101: {
        "name": "Rahul",
        "dept": "CSE",
        "marks": 85
    },

    102: {
        "name": "Amit",
        "dept": "ECE",
        "marks": 72
    },

    103: {
        "name": "Priya",
        "dept": "CSE",
        "marks": 95
    },

    104: {
        "name": "Neha",
        "dept": "IT",
        "marks": 68
    },

    105: {
        "name": "Rohan",
        "dept": "ECE",
        "marks": 88
    }
}


# 1. Sort the dictionary according to marks (highest to lowest)

sorted_student = dict(
    sorted(
        student.items(),
        key=lambda x: x[1]["marks"],
        reverse=True
    )
)

print("Students sorted according to marks:")
for roll, details in sorted_student.items():
    print(roll, details)


# 2. Print the record of the student with highest marks

highest_student = max(
    student.items(),
    key=lambda x: x[1]["marks"]
)

print("\nStudent with highest marks:")
print("Roll Number:", highest_student[0])
print("Record:", highest_student[1])


# 3. Find the average marks of students

total_marks = sum(
    map(lambda x: x["marks"], student.values())
)

average = total_marks / len(student)

print("\nAverage marks:", average)


# 4. Print students who scored more than average

print("\nStudents scoring more than average:")

for roll, details in student.items():
    if details["marks"] > average:
        print(roll, details)