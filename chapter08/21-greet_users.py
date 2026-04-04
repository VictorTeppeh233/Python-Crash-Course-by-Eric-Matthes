# Passing a List to a function

#defining the function
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
    
#creating the list
usernames = ['hannah', 'josephine', 'harriet']

#passing the list to the functions
greet_users(usernames)
