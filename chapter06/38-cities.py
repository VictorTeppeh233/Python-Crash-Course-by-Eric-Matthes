# Assignment 6.11

"""
Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
Create a dictionary of information about each city and include the country that the city is in, 
its approximate population, and one fact about that city. 
The keys for each city’s dictionary should be something like country, population, and fact. 
Print the name of each city and all of the information you have stored about it.
"""

cities = {
    'accra' : {
        "country" : "Ghana",
        "population": " About 2.8 million",
        "fact": "It is the capital city of Ghana.",
    },

    'lagos' : {
        "country" : "Nigeria",
        "population": " About 15 million",
        "fact": "It is one of the largest cities in Africa.",
    },

    'nairobi' : {
        "country" : "Kenya",
        "population": " About 15 million",
        "fact": "It has a national park within the city.",
    }
}

for city, info in cities.items():
    print(f'City: {city.title()}: ')
    print(f'Country: {info['country'].title()}')
    print(f'Population: {info['population']}')
    print(f'Fact: {info['fact']}')
    print('-' * 20)