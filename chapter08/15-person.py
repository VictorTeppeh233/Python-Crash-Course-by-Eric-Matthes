# Returning a Dictionary

#defining the function
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person  = {'first': first_name, 'last': last_name}
    #an if statement to handle when the user provides an age
    if age:
        person['age'] = age
    return person

#assign the return value to musician
musician = build_person('john', 'doe', age=50)
#printing the return value
print(musician)