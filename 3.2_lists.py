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

print(len(prices))  # 5
print(min(prices))  # 76.30
print(max(prices))  # 650.00
print(sum(prices))  # 1203.38
print(prices.index(76.30))  # 0
print(prices.count(650.00))  # 2
