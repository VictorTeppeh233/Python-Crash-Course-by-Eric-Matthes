# Storing Multiple Classes in a Module

"""A set of classes used to represent gas and electric cars."""
#importing the moudle
from car import ElectricCar

#instantiate the class and calling methods
my_nissan = ElectricCar('nissan', 'leaf', 2024)
print(my_nissan.get_descriptive_name())
my_nissan.battery.describe_battery()
my_nissan.battery.get_range()