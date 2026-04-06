# Setting a Default Value for an Attribute

class Car:
    #creating the class
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descripttive name."""
        long_name = f"{self.year} {self.make} {self.model}" 
        return long_name.title()
    
    def read_odometer(self):
        """Print a statment showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

#instantiate the class
my_new_car = Car('audi', 'a4', 2024)
#calling methods on the class
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()