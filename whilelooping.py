# count = 0
# n = int(input('Enter number: '))

# while n > 1:
#     n /= 2
#     count += n

# print(n)
# print(count)


# day = int(input("what day is it "))
# while day < 25:
#     print('There is a window to open in the advent calendar')
#     day += 1  # if the = sign removed, creates infinite loop
#     print(26 - day, 'Day\'s left until Christmas')
# else:
#     print('It is Christmas Day')


# nums = [2, 7, 11, 15]
# target = 9
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i, j)
# user_input = input('Enter numbers: ')
# print(user_input)
# tokens = user_input.split()

# print(tokens)

# nums = []
# for token in tokens:
#     nums.append(int(token))
#     print(nums)
#     print(token)

# print()
# for index in range(len(nums)):
#     value = nums[index]
#     print('%d: %d' % (index, value))

# a = input('enter numbers: ')
# token = a.split()

# nums = []
# for i, token in enumerate(token):
#     nums.append(int(token))
#     if i + i == 6:
#         print(i, i)

num_guesses = 3
user_guesses = []

ask = input('Enter number')
token = ask.split()
for i in len(num_guesses):
    user_guesses.append(token)

print(user_guesses)
