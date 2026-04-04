# Mixing Positional and Arbitrary Arguments

#creating the function
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"Making a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


#calling the function
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extracheese')