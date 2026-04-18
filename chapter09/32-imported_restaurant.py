# assignment 9.10

"""
Using your latest Restaurant class, store it in a module. 
Make a separate file that imports Restaurant. 
Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
"""

# Import the Restaurant class from the restaurant module (restaurant.py file)
from restaurant import Restaurant

# Create an instance (object) of the Restaurant class
my_restaurant = Restaurant("Asanka Kitchen", 'Ghanaian cuisine')

# Call the describe_restaurant method
# This method prints the restaurant's name and cuisine type
my_restaurant.describe_restaurant()