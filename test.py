class Automobile:
    def __init__(self, vehicle, make):
        self.__vehicle = vehicle
        self.__make = make
        # self.__model = model
        # self.__color = color
        # self.__year = year
        # self.__mileage = mileage

    def __add_new_vehicle(self, vehicle):
        self.__vehicle = input('What vehicle would you like to add: ')
        vehicles['Car'] = self.__vehicle

    def __remove_vehicle_quest(self, vehicle):
        print("Would you like to remove your vehicle?,if yes please press Y , if no please press N")
        answer = input()
        if answer == "Y":
            car._Automobile__remove_vehicle('delete')
        if answer == "N":
            print('No vehicle will be deleted', vehicles)

    def __remove_vehicle(self, vehicle):
        del vehicles['Car']


inventory = {}
vehicles = {}
car = Automobile('vehicle 1',
                 'lexus')


def main():
    car._Automobile__add_new_vehicle('add')
    print(vehicles)
    car._Automobile__remove_vehicle_quest('delete')
    print(vehicles)


if __name__ == '__main__':
    main()
