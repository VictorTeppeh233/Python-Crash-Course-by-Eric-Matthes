# Assignment 7.10

"""
Write a program that polls users about their dream vacation. 
Write a prompt similar to 
If you could visit one place in the world, where would you go? 
Include a block of code that prints the results of the poll.
"""
#creating an empty dictionay, it should hold the names as key and answers as values
responses = {}

#Set a flag to show that polling is active
polling_active = True

while polling_active:
    #prompt for the person's name and response
    name = input('\nWhat is your name? ')
    response = input('If you could visit one place in the world, where would you go? ')

    #store the response in the dictionary
    responses[name] = response

    #find out if anyone else wants to take the poll
    repeat = input("Would you like to let another person take the poll? (yes/ no) ")
    if repeat =='no':
        polling_active = False

#show results
print("\n----- Poll Results -----")
#looping through the dictionary
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")