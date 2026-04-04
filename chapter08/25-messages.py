# assignment 8.9

"""
Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message.
"""
#creating the list of messages
short_messages = [
    'I love Ghana.',
    'Ghana is in West Africa.',
    'Accra is the capital of Ghana.',
    'Ghana has 16 Regions.'
]

#creating the function
def show_messages(messages):
    for message in short_messages:
        print(message)

#calling the function
show_messages(short_messages)