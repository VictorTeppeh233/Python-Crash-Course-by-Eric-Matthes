# assignment 9.1

"""
Make a class called Restaurant. 
The __init__() method for Restaurant should store two attributes: 
a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information, 
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
"""

# creating the class
class Restaurant:
    """Printing details of the restaurant and indicate open time"""

    # the constructor method runs when we create a new instance
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print restaurant name and cuisine type"""
        print(f"The restaurant is {self.restaurant_name}.")
        print(f"Cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """Print if the restaurant is open or close"""
        print("The restaurant is open.")

#creating an instance of Restaurant
restaurant_1 = Restaurant("Combat Kitchen", "Continental")

#Calling the methods
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()