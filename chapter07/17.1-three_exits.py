# Assignment 7.6

"""
•Use a conditional test in the while statement to stop the loop.
"""

prompt = "Welcome to Cinemax."
prompt += "\nPlease enter your age (or 'quit' to exit):\n"

age = ""

while age != 'quit':
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