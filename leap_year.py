a = int(input("Enter Year : "))

if a == 0:
    print("Invalid Input!")
elif a % 4:
    print("Leap Year!")
elif a % 100 == 0:
    print("Not a Leap Year.")
elif  a % 400:
    print("Leap Year!")
else :
    print("Not a Leap Year.")