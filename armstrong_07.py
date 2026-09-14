def checkArmstrong(num):
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit ** digits
        num = num // 10

    if total == original:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if checkArmstrong(num):
    print("True - The number is an Armstrong number")
else:
    print("False - The number is not an Armstrong number")