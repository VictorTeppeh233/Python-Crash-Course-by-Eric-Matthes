# Assignment 7.6

"""
•Use a break statement to exit the loop when the user enters a 'quit' value.
"""

prompt = "Welcome to Cinemax."
prompt += "\nPlease enter your age (or 'quit' to exit):\n"

while True:
    age = input(prompt)
    
    if age == 'quit':
        break
    
    age = int(age)
    
    if age < 3:
        price = "free"
    elif age <= 12:
        price = 10
    else:
        price = 15
    
    print(f'The cost of your movie ticket is ${price}.')
    print("-" * 23)