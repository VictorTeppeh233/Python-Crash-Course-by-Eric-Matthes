# Assignment 6.10

"""
Give each person more than 1 favorite number.
Then print each person’s name along with their favorite numbers
"""

fav_number = {
    'ama': [60 , 120, 180],
    'samuel': [9, 18, 20],
    'mena': [3,33,300],
    'sena': [100,75, 90],
    'chief': [50,150, 75]
}

for person, numbers in fav_number.items():
    print(f"{person.title()}'s favorite number is :.")
    for number in numbers:
        print(number)
    print('-' * 20)