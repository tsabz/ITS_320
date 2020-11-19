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


class Starting_Odometer:
    print('What was your starting odemeter reading: ')
    a_odometer = int(input())
    car['Starting Odometer'] = a_odometer


class Ending_Odometer:
    print('What is your ending odometer reading: ')
    b_Odometer = int(input())
    car['Ending Odometer'] = b_Odometer


class Miles_Per_Gallon:
    print('What is your estimated miles per gallon: ')
    mpg = input()
    car['Miles Per Gallon'] = mpg + ' mpg'
    print(car)


def main():
    Car_brand()
    Car_Model()
    Starting_Odometer()
    Ending_Odometer()
    Miles_Per_Gallon()


if __name__ == '__main__':
    main()
