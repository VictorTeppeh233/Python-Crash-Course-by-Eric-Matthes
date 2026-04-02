# assignment

"""
Modify the make_shirt() function so that shirts are
large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, 
and a shirt of any size with a different message
"""

#defining the function
def make_shirt(size='large', message='I love python'):
    print(f'Size: {size}')
    print(f'Message: {message}.')

# calling the function
make_shirt()
make_shirt(size='medium', message='I love Ghana')
make_shirt('small', 'Kids love python too')