x = int(input("Enter a number: "))

temp = x
reverse = 0

if x < 0:
    print("False")
else:
    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10

    if temp == reverse:
        print("True")
    else:
        print("False")