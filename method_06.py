def doSum(num):
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total


num = int(input("Enter a number: "))

result = doSum(num)

print("Sum of digits:", result)