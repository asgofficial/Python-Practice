class Student:

    def __init__(self, name, department, roll_number):
        self.name = name
        self.department = department
        self.roll_number = roll_number

    def show(self):
        print("----------------------")
        print("Name:", self.name)
        print("Department:", self.department)
        print("Roll Number:", self.roll_number)
        print("----------------------")


s1 = Student("Rohul", "CSE", 101)
s2 = Student("Prisha", "ECE", 102)
s3 = Student("Alex", "CSE", 103)
s4 = Student("Dimple", "IT", 104)
s5 = Student("Sanchita", "ME", 105)

s1.show()
s2.show()
s3.show()
s4.show()
s5.show()