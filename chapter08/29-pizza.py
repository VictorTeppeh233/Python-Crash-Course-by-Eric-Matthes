# Passing an Arbitrary Number of Arguments

#creating a function
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print(f'-{topping}')

#calling the function
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')