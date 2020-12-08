# count = 0
# n = int(input('Enter number: '))

# while n > 1:
#     n /= 2
#     count += n

# print(n)
# print(count)


day = int(input("what day is it "))
while day < 25:
    print('There is a window to open in the advent calendar')
    day += 1  # if the = sign removed, creates infinite loop
    print(26 - day, 'Day\'s left until Christmas')
else:
    print('It is Christmas Day')
