# Modifying Attribute Values

# Modifying an Attribute’s Value Through a Method

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
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        """Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

#initialized the class
my_used_car = Car('subaru', 'outback', '2019')
#calling function
print(my_used_car.get_descriptive_name())
#updating the odometer reading
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
#increasing the odometer reading
my_used_car.increment_odometer(100)
my_used_car.read_odometer()