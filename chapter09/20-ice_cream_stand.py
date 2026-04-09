# assignment 9.6

"""
An ice cream stand is a specific kind of restaurant. 
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166).
Either version of the class will work; just pick the one you like better. 
Add an attribute called flavors that stores a list of ice cream flavors. 
Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.
"""

# creating the class
class Restaurant:
    """Printing details of the restaurant and indicate open time"""

    # the constructor method runs when we create a new instance
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Print restaurant name and cuisine type"""
        print(f"The restaurant is {self.restaurant_name}.")
        print(f"Cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """Print if the restaurant is open or close"""
        print("The restaurant is open.")
    
    def set_number_served(self, num_served):
        """Giving the number_served a value"""
        self.number_served = num_served

    def increment_number_served(self, increment):
        """Increase the number of customers served by a certain number"""
        self.number_served += increment

#creating the child class
class IceCreamStand(Restaurant):
    """An attempt to emulate an Ice Cream Stand"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']
    
    def flavors_list(self):
        print(f"These are the flavors {self.flavors}")

#instantiate the class
stand_1 = IceCreamStand("Vic's Bite", "Dessert")
#calling the method from the child class
stand_1.flavors_list()
#calling the method from the parent class
stand_1.open_restaurant()