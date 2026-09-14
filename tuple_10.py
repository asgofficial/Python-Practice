employees = (
    "Rohul", "Alex", "Priya", "Neha", "Rahul",
    "Rohan", "Amit", "Sneha", "Priya", "Karan",
    "Rahul", "Ananya", "Amit", "Riya", "Sneha",
    "Rahul", "Karan", "Amit", "Neha", "Rahul"
)
print("Employee name and frequency:")

for name in set(employees):
    print(name, ":", employees.count(name))


distinct_employees = tuple(set(employees))

print("\nTuple after removing duplicates:")
print(distinct_employees)

print("\nNumber of distinct employees:", len(distinct_employees))


max_frequency = 0
max_employee = ""

for name in distinct_employees:
    frequency = employees.count(name)

    if frequency > max_frequency:
        max_frequency = frequency
        max_employee = name

print("\nEmployee having maximum frequency:", max_employee)
print("Maximum frequency:", max_frequency)

sorted_employees = tuple(sorted(employees))

print("\nTuple in alphabetical order:")
print(sorted_employees)


search_name = input("\nEnter employee name to search: ")

if search_name in employees:
    print(search_name, "exists in the tuple.")
else:
    print(search_name, "does not exist in the tuple.")