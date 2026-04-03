# Returning a Simple Value

#defining the function and the body
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#calling the function
musician = get_formatted_name('jimi', 'hendrix')
print(musician)