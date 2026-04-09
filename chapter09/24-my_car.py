# Importing Classes
# Importing a Single Class
#importing the Car module from car.py
from car import Car

#instantiate the class
my_new_car = Car('audi', 'a4', '2024')
#calling methods
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 25
my_new_car.read_odometer()