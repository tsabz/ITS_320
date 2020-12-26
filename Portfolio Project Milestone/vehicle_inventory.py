class Automobile:
    def __init__(self, make, model, color, year, mileage):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage
        self.inventory = {}

    def __show_car(self):
        print('Car inventory includes: ', self.__make,
              self.__model, self.__color, self.__year, self.__mileage)

    def __add_new_vehicle(self, make, model, color, year, mileage):
        self.inventory['Make'] = make
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage
    # def add_car(self, make):
    #     make = input('Input the make of a car:')
    #     self.__make = make


car = Automobile('lexus', 'es300', 'white', '1998', 35000)


def main():
    print(car._Automobile__show_car())


if __name__ == '__main__':
    main()
