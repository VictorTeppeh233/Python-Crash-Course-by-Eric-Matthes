# Assignment 7.5

"""
A movie theater charges different ticket prices depending on a person’s age. 
If a person is under the age of 3, the ticket is free; 
if they arebetween 3 and 12, the ticket is $10; 
and if they are over age 12, the ticket is $15. 
Write a loop in which you ask users their age, 
and then tell them the cost of their movie ticket.
"""

prompt = "Welcome to Cinemax."
prompt += "\nPlease enter your age.  \n"

while True:
    age = input(prompt)
    age = int(age)
    
    if age < 3:
        price = "free"
    elif 3 <= age <= 12 :
        price = 10
    else:
        price = 15
    
    print(f'The cost of your movie ticket is ${price}.')
    print("-" * 23)