# assignment 8.3

"""
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.
"""

#defining the function
def make_shirt(size, message):
    print(f'Size: {size}')
    print(f'Message: {message.upper()}.')

# calling the function
make_shirt('medium', 'hacktoberfest 2026')
make_shirt(size='large', message='I love Ghana')