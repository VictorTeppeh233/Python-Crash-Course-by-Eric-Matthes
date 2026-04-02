# assignment 8.5

"""
Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. 
Give the parameter for the country a default value.
Call your function for three different cities, 
at least one of which is not in the default country.
"""

#defining a function
def describe_city(name, country="Ghana"):
    print(f"{name.title()} is in {country.title()}.")

describe_city('accra')
describe_city("kumasi")
describe_city("seoul", "South Korea")