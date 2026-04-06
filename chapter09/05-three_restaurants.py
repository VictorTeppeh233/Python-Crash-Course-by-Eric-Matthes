# assignment 9.2

"""
Create three different instances from the class, 
and call describe_restaurant() for each instance.
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
restaurant_2 = Restaurant

#Calling the methods
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()