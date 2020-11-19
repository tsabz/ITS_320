car = {}


class Car_brand:
    print('What is your car brand: ')
    car_brand = input()
    car['Car brand'] = car_brand


class Car_Model:
    print('What is your car model: ')
    car_model = input()
    car['Car Model'] = car_model


class Year:
    print('What is your car year: ')
    year = input()
    car['Year'] = year
    print(car)


def main():
    Car_brand()
    Car_Model()
    Year()


if __name__ == '__main__':
    main()
