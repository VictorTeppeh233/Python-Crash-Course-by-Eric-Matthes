#Importing an Entire Module

#importing the whole car moudle
import car

#instantiate the class and calling methods
my_mustang = car.Car('ford', 'mustang', '2004')
print(my_mustang.get_descriptive_name())

my_nissan = car.ElectricCar('nissan', 'leaf', 2024)
print(my_nissan.get_descriptive_name())