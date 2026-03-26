# Checking for special items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_toppings in requested_toppings:
    if requested_toppings == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_toppings}.")

print("\nFinished making your pizza.")