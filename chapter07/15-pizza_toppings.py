# Assignment 7.4

"""
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
As they enter each topping, print a message saying you’ll add that topping to their pizza.
"""

prompt = "Hello, welcome to Pizza Magic."
prompt += "\nPlease enter a toppings you'd like to be served with your pizza. \n"

while True:
    pizza = input(prompt)
    
    if pizza == 'quit':
        break
    else:
        print(f"Adding {pizza} to your pizza")
    print('-' * 20)
