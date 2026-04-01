# Assignment 6.2

"""
Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. 
Think of a favorite number for each person, and store each as a value in your dictionary. 
Print each person’s name and their favorite number
"""

fav_number = {
    'ama': 60,
    'samuel': 9,
    'mena': 3,
    'sena': 100,
    'chief': 10,
}

for person, number in fav_number.items():
    print(f"{person.title()}'s favorite number is {number}.")