marks = [75, 82, 65, 90, 75, 68, 88, 75, 92, 70,
         75, 81, 64, 75, 85, 73, 75, 69, 80, 75]

# i) Find average marks
avg = sum(marks) / len(marks)
print("Average marks:", avg)

# ii) Find number of students scoring more than average
count = 0

for mark in marks:
    if mark > avg:
        count = count + 1

print("Number of students scoring more than average:", count)

max_count = 0
most_scored_marks = 0

for mark in marks:
    count = marks.count(mark)

    if count > max_count:
        max_count = count
        most_scored_marks = mark

print("Marks scored by maximum students:", most_scored_marks)
print("Number of students who scored these marks:", max_count)