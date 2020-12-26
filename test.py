class Automobile:
    def __init__(self, vehicle, make, model, color, year, mileage):
        self.__vehicle = vehicle
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = int(year)
        self.__mileage = int(mileage)

    def __add_new_vehicle(self, make, model, color, year, mileage):
        self.__vehicle = input('What personal identification number would you like to give your car: ')
        vehicles['Car'] = {}
        self.__make = input('What is the make of your car? ')
        vehicles['Car']['Make'] = self.__make
        self.__model = input('What is the model of your car? ')
        vehicles['Car']['Model'] = self.__model
        self.__color = input('What is the color of your car? ')
        vehicles['Car']['Color'] = self.__color
        self.__year = input('What is the year of your car? ')
        vehicles['Car']['Year'] = self.__year
        self.__mileage = input('What is the mileage of your car? ')
        vehicles['Car']['Mileage'] = self.__mileage


    # def __add_attributes(self, vehicle, make):
    #     vehicles['Car'] = vehicle
        
    #     vehicles['Car']['Make'] = self.__make

    def __vehicle_options(self, vehicle, model, color, year, mileage):
        answer = input('To look at your vehicle press 1, to update your vehicle press 2, to delete your vehicle press 3: ')
        if answer == '1':
            print(vehicles)
        if answer == '3':
            car._Automobile__remove_vehicle_quest(vehicles)
    
    def __remove_vehicle_quest(self, vehicle):
        answer = input('Are you sure you would like to delete your vehicle?, press Y for yes or N for no: ')
        if answer == "Y":
            car._Automobile__remove_vehicle('vehicle','delete')
            print(vehicles)
        if answer == "N":
            print('No vehicle will be deleted', vehicles)

    def __remove_vehicle(self, vehicle, answer):
        del vehicles['Car']

vehicles = {}
car = Automobile('vehicle 1',
                 'lexus', 'es300', 'white', 1998, 35000)


def main():
    car._Automobile__add_new_vehicle('lexus', 'es300','white', 1998, 35000)
    # car._Automobile__add_attributes('vehicle', 'make')
    car._Automobile__vehicle_options('lexus', 'es300','white', 1998, 35000)
    


if __name__ == '__main__':
    main()
