# Assignment 6.7

"""
Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
Loop through your list of people. As you loop through the list, print everything you know about each person.
"""
person_1 = {
    'first_name': 'albert',
    'last_name': 'einstein',
    'age': '98',
    'city': 'princeton',
}

person_2 = {
    'first_name': 'isaac',
    'last_name': 'newton',
    'age': '60',
    'city': 'london',
}

person_3 = {
    'first_name': 'kweku',
    'last_name': 'ananse',
    'age': '120',
    'city': 'kumasi',
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = person['first_name'] + " " + person['last_name']
    print(f'Full name: {full_name.title()}')
    print(f'Age: {person['age']}')
    print(f'City: {person['city'].title()}')
    print('-' * 25)