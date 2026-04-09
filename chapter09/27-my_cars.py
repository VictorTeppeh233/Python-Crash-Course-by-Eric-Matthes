#Importing a Module into a Module

from electric_car import Car
from electric_car import ElectricCar

#instantiate the class and calling methods
my_mustang = Car('ford', 'mustang', '2004')
print(my_mustang.get_descriptive_name())

my_nissan = ElectricCar('nissan', 'leaf', 2024)
print(my_nissan.get_descriptive_name())