# Assignment 6.8

"""
Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. 
Next, loop through your list and as you do, print everything you know about each pet.
"""

pet_1 = {
    'name': 'scooby',
    'type': 'dog',
    'owner': 'shaggy'
}

pet_2 = {
    'name': 'billy',
    'type': 'goat',
    'owner': 'joseph'
}


pet_3 = {
    'name': 'lily',
    'type': 'sheep',
    'owner': 'mary'
}


pet_4 = {
    'name': 'owie',
    'type': 'owl',
    'owner': 'harry'
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f'Pet Name: {pet['name'].title()}.')
    print(f'Pet Type: {pet['type'].title()}.')
    print(f'Pet owner: {pet['owner'].title()}.')
    print('-' * 20)