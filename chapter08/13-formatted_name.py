# Making an Argument Optional

#defining the function and the body
#the middle name is made optional
def get_formatted_name(first_name,  last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

#calling the function
musician = get_formatted_name('jimi', 'hendrix','lee')
print(musician)

musician = get_formatted_name('vivian', 'opoku')
print(musician)