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
