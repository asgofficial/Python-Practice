n = int(input("Enter a Number : "))

fact = 1

if n < 0:
    print("Invalid Input!")
else:
    for i in range(1, n+1):
        fact = fact*i
    print("Factorial : ", fact)