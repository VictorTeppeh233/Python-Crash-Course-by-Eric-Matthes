# Assignment 7.6

"""
•Use an active variable to control how long the loop runs.
"""

prompt = "Welcome to Cinemax."
prompt += "\nPlease enter your age (or 'quit' to exit):\n"

active = True

while active:
    age = input(prompt)
    
    if age == 'quit':
        active = False
    else:
        age = int(age)
        
        if age < 3:
            price = "free"
        elif age <= 12:
            price = 10
        else:
            price = 15
        
        print(f'The cost of your movie ticket is ${price}.')
        print("-" * 23)