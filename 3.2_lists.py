nums = ['1', '2']

nums.append('3')  # ['1', '2', '3']

# print(nums)

nums.pop()  # ['1', '2']

# print(nums)

nums.remove('1')  # ['2']

# print(nums)


prices = [
    34.62, 76.30, 85.05,
    180.05, 90.75, 211.98
]

prices.pop(0)
# print(prices)

prices.remove(90.75)
# print(prices)

prices.append(650.00)
prices.append(650.00)
# print(prices)

# print(len(prices))  # 5
# print(min(prices))  # 76.30
# print(max(prices))  # 650.00
# print(sum(prices))  # 1203.38
# print(prices.index(76.30))  # 0
# print(prices.count(650.00))  # 2

# 3.5
exam1_grade = float(input('Enter score on Exam 1 (out of 100):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 100):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 100):\n'))
exam4_grade = float(input('Enter score on Exam 4 (out of 100):\n'))
exam5_grade = float(input('Enter score on Exam 5 (out of 100):\n'))
exam6_grade = float(input('Enter score on Exam 6 (out of 100):\n'))
exam7_grade = float(input('Enter score on Exam 7 (out of 100):\n'))


exam1 = exam1_grade / 100
exam2 = exam2_grade / 100
exam3 = exam3_grade / 100
exam4 = exam4_grade / 50
exam5 = exam5_grade / 50
exam6 = exam6_grade / 50
exam7 = exam7_grade / 50

sixty_percent = (exam1 + exam2 + exam3) / 3
forty_percent = (exam4 + exam5 + exam6 + exam7) / 4


overall_grade = ((0.6 * sixty_percent) + (0.4 * forty_percent)) * 100


print('Your overall grade is:', overall_grade)
