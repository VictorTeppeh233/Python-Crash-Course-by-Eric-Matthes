# Assignment 6.5

"""
Make a dictionary containing three major rivers and the country each river runs through. 
One key-value pair might be 'nile': 'egypt'.
•Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
•Use a loop to print the name of each river included in the dictionary.
•Use a loop to print the name of each country included in the dictionary.
"""

rivers = {
    "Ghana": 'Black-Volta',
    "USA": 'Missisipi River',
    "Egypt": 'Nile River',
    }

for key, value in rivers.items():
    print(f'\nThe {value} runs through {key}.')

for river in rivers.keys():
    print(f"\n{river}")

for country in rivers.values():
    print(f"\n{country}")