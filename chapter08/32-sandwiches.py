# assignment 8.12

"""
Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides, 
and it should print a summary of the sandwich that’s being ordered. 
Call the function three times, using a different number of arguments each time.
"""

#creating the function
"""Collecting and printing the items the person wants."""
def sandwich_toppings(*toppings):
    print("Making a sandich with these items: ")
    for topping in toppings:
        print(f'- {topping}')

#calling the function
sandwich_toppings('beef')
sandwich_toppings('turkey', 'bacon', 'ham')
sandwich_toppings('tomatoes', 'onions', 'cucumbers', 'cheese', 'lettuce')