# print('Please selects any number greater than 0')
# num_insects = int(input())

# if num_insects > 0:
#     while num_insects * 2 <= 100:
#         num_insects *= 2
#         print(num_insects, end=" ")
i1 = 1
while i1 < 19:
    i2 = 3
    while i2 <= 9:
        print('%d%d' % (i1, i2), end=' ')
        i2 = i2 + 3
    i1 = i1 + 10
