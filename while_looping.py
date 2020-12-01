print('Please selects any number greater than 0')
num_insects = int(input())

if num_insects > 0:
    while num_insects * 2 <= 100:
        num_insects *= 2
        print(num_insects, end=" ")
