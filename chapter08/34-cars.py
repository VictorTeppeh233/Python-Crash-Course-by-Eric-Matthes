#assignment 8.14

"""
Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. 
It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, 
such as a color or an optional feature. 
Your function should work for a call like this one:
"""

# creating the function
def car_info(manufacturer, model_name, **cars):
    cars['manufaturer'] = manufacturer
    cars['model name'] = model_name
    return cars

# call the function with arguments and assigning it.
car_1 = car_info('tesla', 
                 'cyber truck',
                 ceo='elon musk',
                 location='usa',
                 )

print(car_1)