# assignment 8.10

"""
Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() 
that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.
"""

#Initial list of messages and empty list to store sent messages.
short_messages = [
    'I love Ghana.', 
    'Ghana is in West Africa.', 
    'Accra is the capital of Ghana.', 
    'Ghana has 16 Regions.'
]

sent_messages = []

#creating the function
def show_messages(messages):
    while messages:
        current_message = short_messages.pop()
        sent_messages.append(current_message)
        print(f'Sending message: {current_message}')

#calling the function
show_messages(short_messages)

#printing the messages
print('Old messages list:')
print(short_messages)
print('-' * 30)
print('Sent messages list:')
print(sent_messages)