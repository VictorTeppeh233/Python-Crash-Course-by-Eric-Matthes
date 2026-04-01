# Assignment 6.9

"""
Make a dictionary called favorite_places. 
Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
Loop through the dictionary, and print each person’s name and their favorite places.
"""

favorite_places = {
    'mena': ['Tokyo', 'shanghai'],
    'abena': ['boston', 'giza', ],
    'naomi':['maldives', 'shibuya', 'seoul', 'paris'],
}

for persons, places in favorite_places.items():
    print(f"{persons.title()}'s favorite places:")
    for place in places:
        print(f'{place.title()}')
    print('-' * 20)