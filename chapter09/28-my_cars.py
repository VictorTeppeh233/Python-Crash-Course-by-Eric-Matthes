# Using Aliases when importing classes

from electric_car import ElectricCar as EC

my_nissan = EC('nissan', 'leaf', 2024)
my_nissan.battery.get_range()