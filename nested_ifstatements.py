age = int(input("enter number: "))


if age % 2 == 0:
    if age * 5:
        print(age * 5)
        print("number is divisble by 2 and will end with 0")
else:
    if age % 3 == 0:
        if age * 3:
            print(age * 3)
            print("Number is divisble by 3 and will always be odd")
    else:
        print("to be continued")
