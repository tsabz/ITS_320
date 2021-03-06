class Automobile:
    #initilazes class variables
    def __init__(self, vehicle, make, model, color, year, mileage):
        self.__vehicle = vehicle
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = int(year)
        self.__mileage = int(mileage)

# creating vehicles dict 
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

# ask user what they would like to do, whether that be view, update or delete 
    def __vehicle_options(self, make, model, color, year, mileage):
        answer = input('To look at your vehicle press 1, to update your vehicle press 2, to delete your vehicle press 3: ')
        if answer == '1':
            print(vehicles)
        if answer == '2':
            car._Automobile__update_vehicles_options(self, make, model, color, year, mileage)
        if answer == '3':
            car._Automobile__remove_vehicle_quest(vehicles)

# ask user which specific attributes they would like to update
    def __update_vehicles_options(self, vehicle, make, model, color, year, mileage):
        answer = input("If you want to update make press '1', for model press '2', for color press '3', for year press '4', for mileage press '5': ")
        if answer == '1':
            car._Automobile__update_make(self, make)
        if answer == '2':
            car._Automobile__update_model(self, model)
        if answer == '3':
            car._Automobile__update_color(self, color)
        if answer == '4':
            car._Automobile__update_year(self, year)
        if answer == '5':
            car._Automobile__update_mileage(self, mileage)

# all the update functions for the attributes
    def __update_make(self, vehicle, make):
        self.__make = input("What would you like your make to be: ")
        vehicles['Car']['Make'] = self.__make
        print(vehicles)
    
    def __update_model(self, vehicle, model):
        self.__model = input("What would you like your model to be: ")
        vehicles['Car']['Model'] = self.__model
        print(vehicles)

    def __update_color(self, vehicle, color):
        self.__color = input("What would you like your color to be: ")
        vehicles['Car']['Color'] = self.__color
        print(vehicles)
    
    def __update_year(self, vehicle, year):
        self.__year = input("What would you like your year to be: ")
        vehicles['Car']['Year'] = self.__year
        print(vehicles)
    
    def __update_mileage(self, vehicle, mileage):
        self.__mileage = input("What would you like your mileage to be: ")
        vehicles['Car']['Mileage'] = self.__mileage
        print(vehicles)
 
 # ask user if they would like to delete vehicle 
    def __remove_vehicle_quest(self, vehicle):
        answer = input('Are you sure you would like to delete your vehicle?, press Y for yes or N for no: ')
        if answer == "Y":
            car._Automobile__remove_vehicle('vehicle','delete')
            print(vehicles)
        if answer == "N":
            print('No vehicle will be deleted', vehicles)

# delete vehicle function
    def __remove_vehicle(self, vehicle, answer):
        del vehicles['Car']

vehicles = {}
car = Automobile('vehicle 1',
                 'lexus', 'es300', 'white', 1998, 35000)


def main():
    car._Automobile__add_new_vehicle('lexus', 'es300','white', 1998, 35000)
    car._Automobile__vehicle_options('lexus', 'es300','white', 1998, 35000)
    


if __name__ == '__main__':
    main()
