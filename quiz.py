# def modify(my_list):
#     my_list[1] = 99


# my_list = [10, 20, 30]
# modify(my_list)

# print(my_list)


# employee_name = 'N/A'


# def get_name():
#     name = input('Enter employee name:')
#     employee_name = name


# get_name()
# print('Employee name:', employee_name)


# my_var = "This is a variable"


# def my_func():
#     pass


# print(globals())


# def count_down(count):
#     if count == 0:
#         print('Go!')
#     else:
#         print(count)
#         count_down(count-1)


# count_down(2)


# def avg(a, b):
#     tmp = (a + b) / 2.0  # Creates tmp in local namespace
#     return tmp


# a = 5
# b = 10

# tmp = a + b  # Creates tmp in global namespace
# x = avg(a, b)

# print('Avg: %f' % tmp)


# player_name = 'Gandalf'
# player_type = 'Wizard'


# def roll():
#     """Returns a roll of a 20-sided die"""
#     number = random.randint(1, 20)
#     return number


# print('A troll attacks!')
# troll_roll = roll()
# player_roll = roll()

# print('Player: %s Troll: %s' % (str(player_roll), str(troll_roll)))


# def sandwich(bread, meat, *args):
#     print('%s on %s' % (meat, bread), end=' ')
#     if len(args) > 0:
#         print('with', end=' ')
#         for extra in args:
#             print(extra, end=' ')
#             print("")


# sandwich('sourdough', 'spam', 'mayo')


# url = 'http://en.wikipedia.org/wiki/Turing'
# domain = url[7:23]
# print(domain)


# my_list = [[25], [15, 25, 35], [10, 15]]
# sorted_list = sorted(my_list, key=max)
# print('Sorted list:', sorted_list)


# user_input = input('Enter numbers:')
# tokens = user_input.split()  # Split into separate strings

# nums = []
# for token in tokens:
#     nums.append(int(token))

# max_num = None
# for num in nums:
#     if (max_num == None) and (num % 2 == 0):
#         max_num = num
#     elif (max_num != None) and (num > max_num) and (num % 2 == 0):
#         max_num = num

# print('Max #:', max_num)


my_dict = dict(bananas=1.59, fries=2.39, burger=3.50, sandwich=2.99)
my_dict.update(dict(soda=1.49, burger=3.69))
burger_price = my_dict.get('burger', 0)
print(burger_price)
