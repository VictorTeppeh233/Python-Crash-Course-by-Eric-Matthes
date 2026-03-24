#Assignment 5.2

"""
Have at least one True and one False result for each of the following:
•Tests for equality and inequality with strings
•Tests using the lower() method
•Numerical tests involving equality and inequality, greater than and less
 than, greater than or equal to, and less than or equal to
•Tests using the and keyword and the or keyword
•Test whether an item is in a list
•Test whether an item is not in a list
"""

name = "Victor"
print("Name is Victor")
print()
print("Is name Victor")
print(name == "Victor")

print()

print("Is name Naomi")
print(name == "Naomi")

print()

print("Is Victor.lower() the same as victor")
print(name.lower() == 'victor')

print()

print("Is 100 above 98")
print(100 > 98)

print()

print("Is 3 less than 1")
print(3 < 1)

print()

print("Is 5 greater than 4 and less than 20")
print(5 > 4 and 5 < 20)

print()

print("Is 25 greater than 4 and less than 20")
print(25 > 4 and 25 < 20)

print()

print("Is 25 greater than 4 or less than 20")
print(25 > 4 or 25 < 20)

countries = ['Ghana', 'Nigeria', 'Togo']
print()
print('Is Ghana in the list')
print("Ghana" in countries )

print()
print("Is Japan not in list")
print("Japan" not in countries)