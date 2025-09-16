#Use a variable to represent a person’s name,
#and include some whitespace characters at the beginning and end of the name

#assigning the name to the variable
name = "  \n\tJohn \n\tKwame \n\tDoe  "

#removing whitespace from the right side
print(name.rstrip())

#removing whitespace from the left side
print(name.lstrip())

#removing white space from both ends
print(name.strip())
