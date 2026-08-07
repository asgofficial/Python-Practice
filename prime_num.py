def isPrime(num):
    if num <= 1:
        return False

    for i in range (2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

num = int(input("Enter a Number : "))

if isPrime(num):
    print("Prime Number!")
else:
    print("Not a Prime Number.")