# assignment 9.4 

"""
Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, 
and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of customers that have been served. 
Call this method with a new number and print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a day of business.
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

#creating an instance of Restaurant
restaurant_1 = Restaurant("Combat Kitchen", "Continental")

#Printing the number of customers served
print(f"{restaurant_1.number_served}")

#changing the number of customers served directly
restaurant_1.number_served = 30

#Printing the number of customers served
print(f"{restaurant_1.number_served}")

#changeing the value of number_served by a method
restaurant_1.set_number_served(50)
#Printing the number of customers served
print(f"{restaurant_1.number_served}")

#increase the number of customers served by the argument
restaurant_1.increment_number_served(25)

#Printing the number of customers served
print(f"{restaurant_1.number_served}")