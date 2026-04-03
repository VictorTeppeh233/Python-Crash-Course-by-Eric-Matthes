# assignment 8.6
# city names

"""
Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this: "Santiago, Chile"
Call your function with at least three city-country pairs, and print the values that are returned.
"""
#defining the function
def city_country(city, country):
    city = (f'"{city.title()}, {country.title()}"')
    print(city)

#calling the function with arguments.
city_country('accra', 'ghana')
city_country('lagos', 'nigeria')
city_country('seoul', 'south korea')
